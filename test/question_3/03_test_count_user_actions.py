from pyspark.sql.functions import col, count, max, expr


def test_count_user_actions(spark):
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

    df = spark.createDataFrame(data, columns)

    df = df.withColumn(
        "time_stamp",
        col("time_stamp").cast("timestamp")
    )

    latest_timestamp = df.select(
        max("time_stamp")
    ).collect()[0][0]

    last_7_days = df.filter(
        col("time_stamp") >= latest_timestamp - expr("INTERVAL 7 DAYS")
    )

    result = (
        last_7_days
        .groupBy("user_id")
        .agg(count("*").alias("action_count"))
    )

    result_data = {
        row["user_id"]: row["action_count"]
        for row in result.collect()
    }

    assert result_data == {
        101: 3,
        102: 3,
        103: 2
    }