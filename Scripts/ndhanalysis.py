from pyspark.sql import SparkSession
from pyspark.sql.types import *

spark = SparkSession.builder \
    .appName("MovieLens100K_Analysis") \
    .getOrCreate()

print("=" * 60)
print("Module 2: Spark SQL Analysis Started")
print("Spark Version:", spark.version)
print("=" * 60)

HDFS_PATH = "hdfs:///user/maria_dev/movielens100k"

# ------------------------------------------------------------
# Read RDDs from HDFS
# ------------------------------------------------------------

user_rdd = spark.sparkContext.textFile(HDFS_PATH + "/u.user")
rating_rdd = spark.sparkContext.textFile(HDFS_PATH + "/u.data")
movie_rdd = spark.sparkContext.textFile(HDFS_PATH + "/u.item")

# ------------------------------------------------------------
# Define Schemas
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
# Convert RDDs to DataFrames
# ------------------------------------------------------------

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

print("\nData loaded successfully")
print("Users:", users_df.count())
print("Ratings:", ratings_df.count())
print("Movies:", movies_df.count())

# ------------------------------------------------------------
# Create Spark SQL Views
# ------------------------------------------------------------

users_df.createOrReplaceTempView("users")
ratings_df.createOrReplaceTempView("ratings")
movies_df.createOrReplaceTempView("movies")

print("\nSpark SQL views created")
spark.sql("SHOW TABLES").show()

# ============================================================
# Task 1: Average Rating for Each Movie
# ============================================================

print("\nTASK 1: Average Rating for Each Movie")

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
    ORDER BY average_rating DESC, total_ratings DESC
""")

task1_df.show(10, truncate=False)

print("""
Interpretation:
The result shows the average rating for each movie. Average rating should be interpreted
together with total ratings because movies with very few ratings may appear highly ranked
but may not strongly represent overall user preference.
""")

# ============================================================
# Task 2: Top 10 Movies with Highest Average Ratings
# ============================================================

print("\nTASK 2: Top Ten Movies with Highest Average Ratings")

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

task2_df.show(truncate=False)

print("""
Interpretation:
The top ten movies are ranked based on average rating. The total number of ratings is
included as a supporting indicator because a movie rated by more users provides stronger
evidence of general audience preference.
""")

# ============================================================
# Task 3: Active Users and Favourite Genre
# ============================================================

print("\nTASK 3: Users Rated At Least 50 Movies and Favourite Genre")

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

movie_genres_query = " UNION ALL ".join(genre_queries)

movie_genres_df = spark.sql(movie_genres_query)
movie_genres_df.createOrReplaceTempView("movie_genres")

task3_df = spark.sql("""
    WITH active_users AS (
        SELECT
            user_id,
            COUNT(movie_id) AS total_movies_rated
        FROM ratings
        GROUP BY user_id
        HAVING COUNT(movie_id) >= 50
    ),

    user_genre_counts AS (
        SELECT
            r.user_id,
            mg.genre,
            COUNT(*) AS genre_frequency
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
    ORDER BY au.total_movies_rated DESC
""")

task3_df.show(10, truncate=False)

print("""
Interpretation:
Active users are users who rated at least 50 movies. Their favourite genre is determined
by the genre that appears most frequently among the movies they rated. This provides a
simple behavioural profile of frequent users.
""")

# ============================================================
# Task 4: Users Less Than 20 Years Old
# ============================================================

print("\nTASK 4: Users Less Than 20 Years Old")

task4_df = spark.sql("""
    SELECT
        user_id,
        age,
        gender,
        occupation,
        zip_code
    FROM users
    WHERE age < 20
    ORDER BY age ASC, user_id ASC
""")

task4_df.show(50, truncate=False)

print("""
Interpretation:
The result identifies users below 20 years old. This group may represent younger movie
viewers and can be used for further age-based preference analysis.
""")

# ============================================================
# Task 5: Scientist Users Aged Between 30 and 40
# ============================================================

print("\nTASK 5: Scientist Users Aged Between 30 and 40")

task5_df = spark.sql("""
    SELECT
        user_id,
        age,
        gender,
        occupation,
        zip_code
    FROM users
    WHERE occupation = 'scientist'
      AND age BETWEEN 30 AND 40
    ORDER BY age ASC, user_id ASC
""")

task5_df.show(truncate=False)

print("""
Interpretation:
The result filters users whose occupation is scientist and whose age is between 30 and 40.
This demonstrates how Spark SQL can support targeted demographic segmentation.
""")

# ------------------------------------------------------------
# Save outputs into HDFS for reproducibility
# ------------------------------------------------------------

print("\nSaving analysis outputs into HDFS...")

OUTPUT_PATH = "hdfs:///user/maria_dev/movielens100k_outputs"

task1_df.coalesce(1).write.mode("overwrite").option("header", "true").csv(OUTPUT_PATH + "/task1_average_ratings")
task2_df.coalesce(1).write.mode("overwrite").option("header", "true").csv(OUTPUT_PATH + "/task2_top10_movies")
task3_df.coalesce(1).write.mode("overwrite").option("header", "true").csv(OUTPUT_PATH + "/task3_favourite_genres")
task4_df.coalesce(1).write.mode("overwrite").option("header", "true").csv(OUTPUT_PATH + "/task4_young_users")
task5_df.coalesce(1).write.mode("overwrite").option("header", "true").csv(OUTPUT_PATH + "/task5_scientist_users")

print("Outputs saved successfully at:")
print(OUTPUT_PATH)

print("\nModule 2 Completed Successfully")

spark.stop()
