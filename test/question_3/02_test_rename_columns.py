def test_rename_columns(spark):
    data = [
        (1, 101, "login", "2023-09-05 08:30:00"),
        (2, 102, "click", "2023-09-06 12:45:00")
    ]

    columns = ["log id", "user$id", "action", "timestamp"]

    df = spark.createDataFrame(data, columns)

    new_columns = [
        "log_id",
        "user_id",
        "user_activity",
        "time_stamp"
    ]

    for old_name, new_name in zip(df.columns, new_columns):
        df = df.withColumnRenamed(old_name, new_name)

    assert df.columns == [
        "log_id",
        "user_id",
        "user_activity",
        "time_stamp"
    ]