from pyspark.sql import SparkSession
from pyspark.sql.types import *
import subprocess

KEYSPACE = "movielens_db"
CASSANDRA_HOST = "127.0.0.1"
CASSANDRA_PORT = "9042"
CQLSH_PATH = "/opt/cassandra/bin/cqlsh"

HDFS_PATH = "hdfs:///user/maria_dev/movielens100k"
OUTPUT_PATH = "hdfs:///user/maria_dev/movielens100k_outputs"

# ------------------------------------------------------------
# Create Cassandra keyspace and tables
# ------------------------------------------------------------

cql_script = """
CREATE KEYSPACE IF NOT EXISTS movielens_db
WITH replication = {
'class': 'SimpleStrategy',
'replication_factor': 1
};

USE movielens_db;

CREATE TABLE IF NOT EXISTS users (
    user_id int PRIMARY KEY,
    age int,
    gender text,
    occupation text,
    zip_code text
);

CREATE TABLE IF NOT EXISTS ratings (
    user_id int,
    movie_id int,
    rating int,
    timestamp int,
    PRIMARY KEY (user_id, movie_id)
);

CREATE TABLE IF NOT EXISTS movies (
    movie_id int PRIMARY KEY,
    movie_title text,
    release_date text,
    video_release_date text,
    imdb_url text,
    unknown int,
    action int,
    adventure int,
    animation int,
    children int,
    comedy int,
    crime int,
    documentary int,
    drama int,
    fantasy int,
    film_noir int,
    horror int,
    musical int,
    mystery int,
    romance int,
    sci_fi int,
    thriller int,
    war int,
    western int
);

CREATE TABLE IF NOT EXISTS task1_average_ratings (
    movie_id int PRIMARY KEY,
    movie_title text,
    average_rating double,
    total_ratings bigint
);

CREATE TABLE IF NOT EXISTS task2_top10_movies (
    rank_no int PRIMARY KEY,
    movie_id int,
    movie_title text,
    average_rating double,
    total_ratings bigint
);

CREATE TABLE IF NOT EXISTS task3_favourite_genres (
    user_id int PRIMARY KEY,
    total_movies_rated bigint,
    favourite_genre text,
    genre_frequency bigint
);

CREATE TABLE IF NOT EXISTS task4_young_users (
    user_id int PRIMARY KEY,
    age int,
    gender text,
    occupation text,
    zip_code text
);

CREATE TABLE IF NOT EXISTS task5_scientist_users (
    user_id int PRIMARY KEY,
    age int,
    gender text,
    occupation text,
    zip_code text
);
"""

with open("/tmp/ndh_cassandra_setup.cql", "w") as file:
    file.write(cql_script)

print("Creating Cassandra keyspace and tables...")
subprocess.call([CQLSH_PATH, CASSANDRA_HOST, CASSANDRA_PORT, "-f", "/tmp/ndh_cassandra_setup.cql"])
print("Cassandra keyspace and tables created successfully.")

# ------------------------------------------------------------
# Create Spark Session with Cassandra connector
# ------------------------------------------------------------

spark = SparkSession.builder \
    .appName("MovieLens100K_Cassandra_Integration") \
    .config("spark.cassandra.connection.host", CASSANDRA_HOST) \
    .config("spark.cassandra.connection.port", CASSANDRA_PORT) \
    .getOrCreate()

print("=" * 60)
print("Module 3: Cassandra Integration Started")
print("Spark Version:", spark.version)
print("=" * 60)

# ------------------------------------------------------------
# Define schemas
# ------------------------------------------------------------

user_schema = StructType([
    StructField("user_id", IntegerType(), False),
    StructField("age", IntegerType(), True),
    StructField("gender", StringType(), True),
    StructField("occupation", StringType(), True),
    StructField("zip_code", StringType(), True)
])

rating_schema = StructType([
    StructField("user_id", IntegerType(), False),
    StructField("movie_id", IntegerType(), False),
    StructField("rating", IntegerType(), True),
    StructField("timestamp", IntegerType(), True)
])

movie_schema = StructType([
    StructField("movie_id", IntegerType(), False),
    StructField("movie_title", StringType(), True),
    StructField("release_date", StringType(), True),
    StructField("video_release_date", StringType(), True),
    StructField("imdb_url", StringType(), True),
    StructField("unknown", IntegerType(), True),
    StructField("action", IntegerType(), True),
    StructField("adventure", IntegerType(), True),
    StructField("animation", IntegerType(), True),
    StructField("children", IntegerType(), True),
    StructField("comedy", IntegerType(), True),
    StructField("crime", IntegerType(), True),
    StructField("documentary", IntegerType(), True),
    StructField("drama", IntegerType(), True),
    StructField("fantasy", IntegerType(), True),
    StructField("film_noir", IntegerType(), True),
    StructField("horror", IntegerType(), True),
    StructField("musical", IntegerType(), True),
    StructField("mystery", IntegerType(), True),
    StructField("romance", IntegerType(), True),
    StructField("sci_fi", IntegerType(), True),
    StructField("thriller", IntegerType(), True),
    StructField("war", IntegerType(), True),
    StructField("western", IntegerType(), True)
])

# ------------------------------------------------------------
# Read raw data from HDFS and convert to DataFrames
# ------------------------------------------------------------

user_rdd = spark.sparkContext.textFile(HDFS_PATH + "/u.user")
rating_rdd = spark.sparkContext.textFile(HDFS_PATH + "/u.data")
movie_rdd = spark.sparkContext.textFile(HDFS_PATH + "/u.item")

users_df = spark.createDataFrame(
    user_rdd.map(lambda x: x.split("|"))
            .map(lambda x: (int(x[0]), int(x[1]), x[2], x[3], x[4])),
    user_schema
).dropDuplicates(["user_id"])

ratings_df = spark.createDataFrame(
    rating_rdd.map(lambda x: x.split("\t"))
              .map(lambda x: (int(x[0]), int(x[1]), int(x[2]), int(x[3]))),
    rating_schema
).dropDuplicates(["user_id", "movie_id"])

movies_df = spark.createDataFrame(
    movie_rdd.map(lambda x: x.split("|"))
             .map(lambda x: (
                 int(x[0]), x[1], x[2], x[3], x[4],
                 int(x[5]), int(x[6]), int(x[7]), int(x[8]), int(x[9]),
                 int(x[10]), int(x[11]), int(x[12]), int(x[13]),
                 int(x[14]), int(x[15]), int(x[16]), int(x[17]),
                 int(x[18]), int(x[19]), int(x[20]), int(x[21]),
                 int(x[22]), int(x[23])
             )),
    movie_schema
).dropDuplicates(["movie_id"])

print("\nDataFrames loaded from HDFS")
print("Users:", users_df.count())
print("Ratings:", ratings_df.count())
print("Movies:", movies_df.count())

# ------------------------------------------------------------
# Write main DataFrames to Cassandra
# ------------------------------------------------------------

print("\nWriting main DataFrames to Cassandra...")

users_df.write.format("org.apache.spark.sql.cassandra") \
    .mode("append") \
    .options(table="users", keyspace=KEYSPACE) \
    .save()

ratings_df.write.format("org.apache.spark.sql.cassandra") \
    .mode("append") \
    .options(table="ratings", keyspace=KEYSPACE) \
    .save()

movies_df.write.format("org.apache.spark.sql.cassandra") \
    .mode("append") \
    .options(table="movies", keyspace=KEYSPACE) \
    .save()

print("Main DataFrames written successfully.")

# ------------------------------------------------------------
# Recreate Spark SQL views for analytical results
# ------------------------------------------------------------

users_df.createOrReplaceTempView("users")
ratings_df.createOrReplaceTempView("ratings")
movies_df.createOrReplaceTempView("movies")

task1_df = spark.sql("""
    SELECT
        m.movie_id,
        m.movie_title,
        ROUND(AVG(r.rating), 3) AS average_rating,
        COUNT(r.rating) AS total_ratings
    FROM ratings r
    INNER JOIN movies m
        ON r.movie_id = m.movie_id
    GROUP BY m.movie_id, m.movie_title
""")

task2_df = spark.sql("""
    SELECT
        ROW_NUMBER() OVER (ORDER BY AVG(r.rating) DESC, COUNT(r.rating) DESC) AS rank_no,
        m.movie_id,
        m.movie_title,
        ROUND(AVG(r.rating), 3) AS average_rating,
        COUNT(r.rating) AS total_ratings
    FROM ratings r
    INNER JOIN movies m
        ON r.movie_id = m.movie_id
    GROUP BY m.movie_id, m.movie_title
    ORDER BY average_rating DESC, total_ratings DESC
    LIMIT 10
""")

genre_columns = [
    "unknown", "action", "adventure", "animation", "children", "comedy",
    "crime", "documentary", "drama", "fantasy", "film_noir", "horror",
    "musical", "mystery", "romance", "sci_fi", "thriller", "war", "western"
]

genre_queries = []

for genre in genre_columns:
    genre_queries.append("""
        SELECT movie_id, movie_title, '{0}' AS genre
        FROM movies
        WHERE {0} = 1
    """.format(genre))

movie_genres_df = spark.sql(" UNION ALL ".join(genre_queries))
movie_genres_df.createOrReplaceTempView("movie_genres")

task3_df = spark.sql("""
    WITH active_users AS (
        SELECT user_id, COUNT(movie_id) AS total_movies_rated
        FROM ratings
        GROUP BY user_id
        HAVING COUNT(movie_id) >= 50
    ),
    user_genre_counts AS (
        SELECT r.user_id, mg.genre, COUNT(*) AS genre_frequency
        FROM ratings r
        INNER JOIN active_users au
            ON r.user_id = au.user_id
        INNER JOIN movie_genres mg
            ON r.movie_id = mg.movie_id
        GROUP BY r.user_id, mg.genre
    ),
    ranked_genres AS (
        SELECT
            user_id,
            genre,
            genre_frequency,
            ROW_NUMBER() OVER (
                PARTITION BY user_id
                ORDER BY genre_frequency DESC, genre ASC
            ) AS genre_rank
        FROM user_genre_counts
    )
    SELECT
        rg.user_id,
        au.total_movies_rated,
        rg.genre AS favourite_genre,
        rg.genre_frequency
    FROM ranked_genres rg
    INNER JOIN active_users au
        ON rg.user_id = au.user_id
    WHERE rg.genre_rank = 1
""")

task4_df = spark.sql("""
    SELECT user_id, age, gender, occupation, zip_code
    FROM users
    WHERE age < 20
""")

task5_df = spark.sql("""
    SELECT user_id, age, gender, occupation, zip_code
    FROM users
    WHERE occupation = 'scientist'
      AND age BETWEEN 30 AND 40
""")

# ------------------------------------------------------------
# Write analytical results to Cassandra
# ------------------------------------------------------------

print("\nWriting analytical result tables to Cassandra...")

task1_df.write.format("org.apache.spark.sql.cassandra") \
    .mode("append") \
    .options(table="task1_average_ratings", keyspace=KEYSPACE) \
    .save()

task2_df.write.format("org.apache.spark.sql.cassandra") \
    .mode("append") \
    .options(table="task2_top10_movies", keyspace=KEYSPACE) \
    .save()

task3_df.write.format("org.apache.spark.sql.cassandra") \
    .mode("append") \
    .options(table="task3_favourite_genres", keyspace=KEYSPACE) \
    .save()

task4_df.write.format("org.apache.spark.sql.cassandra") \
    .mode("append") \
    .options(table="task4_young_users", keyspace=KEYSPACE) \
    .save()

task5_df.write.format("org.apache.spark.sql.cassandra") \
    .mode("append") \
    .options(table="task5_scientist_users", keyspace=KEYSPACE) \
    .save()

print("Analytical result tables written successfully.")

# ------------------------------------------------------------
# Read Cassandra tables back into Spark for validation
# ------------------------------------------------------------

print("\nReading Cassandra tables back into Spark for validation...")

tables = [
    "users",
    "ratings",
    "movies",
    "task1_average_ratings",
    "task2_top10_movies",
    "task3_favourite_genres",
    "task4_young_users",
    "task5_scientist_users"
]

for table in tables:
    df = spark.read.format("org.apache.spark.sql.cassandra") \
        .options(table=table, keyspace=KEYSPACE) \
        .load()

    print(table, ":", df.count(), "rows")
    df.show(5, truncate=False)

print("\nModule 3 Completed Successfully")

spark.stop()
