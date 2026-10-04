def test_create_managed_table(spark):
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

    spark.sql("CREATE DATABASE IF NOT EXISTS test_user")

    df.write \
        .mode("overwrite") \
        .saveAsTable("test_user.login_details_test")

    result = spark.sql(
        "SELECT * FROM test_user.login_details_test"
    )

    assert result.count() == 2

    spark.sql(
        "DROP TABLE test_user.login_details_test"
    )