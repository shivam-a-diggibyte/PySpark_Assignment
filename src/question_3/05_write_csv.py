from pyspark.sql import SparkSession


spark = (
    SparkSession.builder
    .appName("Write Login CSV")
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


login_df.write \
    .mode("overwrite") \
    .option("header", True) \
    .option("delimiter", ",") \
    .option("quote", '"') \
    .csv("output/login_details")


spark.stop()