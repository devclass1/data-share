# 1. Load the dataset
movies_df = spark.read.csv(
    "/Volumes/workspace/default/vol1/moviesDB.csv",
    header=True,
    inferSchema=True
)

# 2. Inspect schema and preview
movies_df.printSchema()
display(movies_df.limit(5))   # Databricks friendly preview

# 3. Select specific columns
display(movies_df.select("title", "year", "Rating").limit(10))

# 4. Filter: Movies released after 2000 with rating >= 8
high_rated_recent = movies_df.filter(
    (movies_df.year > 2000) & (movies_df.Rating >= 8)
)
display(high_rated_recent.limit(10))

# 5. Average rating by genre
from pyspark.sql.functions import split, explode, col, avg

genre_df = movies_df.withColumn("genre", explode(split(col("genres"), "\|")))

avg_genre_rating = genre_df.groupBy("genre").agg(avg("Rating").alias("avg_rating"))
display(avg_genre_rating.orderBy(col("avg_rating").desc()))

# 6. Top 10 movies by Rotten Tomato score
top_rotten = movies_df.orderBy(col("Rotton Tomato").desc()) \
                      .select("title", "Rotton Tomato")
display(top_rotten.limit(10))

# 7. Save results back to Volumes
avg_genre_rating.write.mode("overwrite").csv(
    "/Volumes/workspace/default/vol1/output/avg_genre_rating",
    header=True
)
