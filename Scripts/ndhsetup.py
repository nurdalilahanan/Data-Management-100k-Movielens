from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import col, count, when

# ------------------------------------------------------------
# Create Spark Session
# ------------------------------------------------------------

spark = SparkSession.builder \
    .appName("MovieLens100K_Setup") \
    .getOrCreate()

print("=" * 60)
print("Spark Session Created Successfully")
print("Spark Version :", spark.version)
print("=" * 60)

# ------------------------------------------------------------
# HDFS Location
# ------------------------------------------------------------

HDFS_PATH = "hdfs:///user/maria_dev/movielens100k"

# ------------------------------------------------------------
# Read MovieLens Files from HDFS
# ------------------------------------------------------------

print("\nReading files from HDFS...")

user_rdd = spark.sparkContext.textFile(HDFS_PATH + "/u.user")
rating_rdd = spark.sparkContext.textFile(HDFS_PATH + "/u.data")
movie_rdd = spark.sparkContext.textFile(HDFS_PATH + "/u.item")

print("Files loaded successfully.")

# ------------------------------------------------------------
# Preview RDD
# ------------------------------------------------------------

print("\nSample User Record")
print(user_rdd.first())

print("\nSample Rating Record")
print(rating_rdd.first())

print("\nSample Movie Record")
print(movie_rdd.first())

# ------------------------------------------------------------
# User Schema
# ------------------------------------------------------------

user_schema = StructType([
    StructField("user_id", IntegerType(), False),
    StructField("age", IntegerType(), True),
    StructField("gender", StringType(), True),
    StructField("occupation", StringType(), True),
    StructField("zip_code", StringType(), True)
])

# ------------------------------------------------------------
# Rating Schema
# ------------------------------------------------------------

rating_schema = StructType([
    StructField("user_id", IntegerType(), False),
    StructField("movie_id", IntegerType(), False),
    StructField("rating", IntegerType(), True),
    StructField("timestamp", IntegerType(), True)
])

# ------------------------------------------------------------
# Movie Schema
# ------------------------------------------------------------

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
# Convert User RDD
# ------------------------------------------------------------

users_df = spark.createDataFrame(
    user_rdd.map(lambda x: x.split("|"))
            .map(lambda x: (
                int(x[0]),
                int(x[1]),
                x[2],
                x[3],
                x[4]
            )),
    user_schema
)

# ------------------------------------------------------------
# Convert Rating RDD
# ------------------------------------------------------------

ratings_df = spark.createDataFrame(
    rating_rdd.map(lambda x: x.split("\t"))
              .map(lambda x: (
                  int(x[0]),
                  int(x[1]),
                  int(x[2]),
                  int(x[3])
              )),
    rating_schema
)

# ------------------------------------------------------------
# Convert Movie RDD
# ------------------------------------------------------------

movies_df = spark.createDataFrame(
    movie_rdd.map(lambda x: x.split("|"))
             .map(lambda x: (
                 int(x[0]),
                 x[1],
                 x[2],
                 x[3],
                 x[4],
                 int(x[5]),
                 int(x[6]),
                 int(x[7]),
                 int(x[8]),
                 int(x[9]),
                 int(x[10]),
                 int(x[11]),
                 int(x[12]),
                 int(x[13]),
                 int(x[14]),
                 int(x[15]),
                 int(x[16]),
                 int(x[17]),
                 int(x[18]),
                 int(x[19]),
                 int(x[20]),
                 int(x[21]),
                 int(x[22]),
                 int(x[23])
             )),
    movie_schema
)

# ------------------------------------------------------------
# Show Data
# ------------------------------------------------------------

print("\nUsers Data")
users_df.show(5)

print("\nRatings Data")
ratings_df.show(5)

print("\nMovies Data")
movies_df.show(5)

# ------------------------------------------------------------
# Record Count
# ------------------------------------------------------------

print("\nDataset Summary")

print("Users :", users_df.count())
print("Ratings :", ratings_df.count())
print("Movies :", movies_df.count())

# ------------------------------------------------------------
# Remove Duplicates
# ------------------------------------------------------------

users_df = users_df.dropDuplicates(["user_id"])
ratings_df = ratings_df.dropDuplicates(["user_id","movie_id"])
movies_df = movies_df.dropDuplicates(["movie_id"])

print("\nAfter Removing Duplicates")

print("Users :", users_df.count())
print("Ratings :", ratings_df.count())
print("Movies :", movies_df.count())

# ------------------------------------------------------------
# Missing Values
# ------------------------------------------------------------

print("\nMissing Values")

users_df.select([
    count(when(col(c).isNull(), c)).alias(c)
    for c in users_df.columns
]).show()

ratings_df.select([
    count(when(col(c).isNull(), c)).alias(c)
    for c in ratings_df.columns
]).show()

movies_df.select([
    count(when(col(c).isNull(), c)).alias(c)
    for c in movies_df.columns
]).show()

# ------------------------------------------------------------
# Register SQL Views
# ------------------------------------------------------------

users_df.createOrReplaceTempView("users")
ratings_df.createOrReplaceTempView("ratings")
movies_df.createOrReplaceTempView("movies")

print("\nSpark SQL Views Created")

spark.sql("SHOW TABLES").show()

print("\nModule 1 Completed Successfully")

spark.stop()
