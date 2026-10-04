from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, max, expr


spark = (
    SparkSession.builder
    .appName("Count User Actions")
    .master("local[*]")
    .getOrCreate()
)


data = [
    (1, 101, "login", "2023-09-05 08:30:00"),
    (2, 102, "click", "2023-09-06 12:45:00"),
    (3, 101, "click", "2023-09-07 14:15:00"),
    (4, 103, "login", "2023-09-08 09:00:00"),
    (5, 102, "logout", "2023-09-09 17:30:00"),
    (6, 101, "click", "2023-09-10 11:20:00"),
    (7, 103, "click", "2023-09-11 10:15:00"),
    (8, 102, "click", "2023-09-12 13:10:00")
]

columns = [
    "log_id",
    "user_id",
    "user_activity",
    "time_stamp"
]

login_df = spark.createDataFrame(data, columns)

# Convert string to timestamp
login_df = login_df.withColumn(
    "time_stamp",
    col("time_stamp").cast("timestamp")
)

# Get latest timestamp
latest_timestamp = login_df.select(
    max("time_stamp")
).collect()[0][0]

# Filter last 7 days
last_7_days_df = login_df.filter(
    col("time_stamp") >= latest_timestamp - expr("INTERVAL 7 DAYS")
)

# Count actions per user
result_df = (
    last_7_days_df
    .groupBy("user_id")
    .agg(count("*").alias("action_count"))
)

result_df.show()

spark.stop()