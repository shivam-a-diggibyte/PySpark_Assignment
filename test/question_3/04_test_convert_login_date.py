from pyspark.sql.functions import col, to_date


def test_convert_login_date(spark):
    data = [
        (1, 101, "login", "2023-09-05 08:30:00"),
        (2, 102, "click", "2023-09-06 12:45:00")
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

    df = df.withColumn(
        "login_date",
        to_date("time_stamp", "yyyy-MM-dd")
    )

    assert "login_date" in df.columns

    result = [row["login_date"] for row in df.collect()]

    assert str(result[0]) == "2023-09-05"
    assert str(result[1]) == "2023-09-06"
    