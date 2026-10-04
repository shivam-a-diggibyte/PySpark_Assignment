def test_write_csv(spark, tmp_path):
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

    output_path = str(tmp_path / "login_details")

    df.write \
        .mode("overwrite") \
        .option("header", True) \
        .option("delimiter", ",") \
        .option("quote", '"') \
        .csv(output_path)

    # Read the generated CSV
    result = spark.read \
        .option("header", True) \
        .csv(output_path)

    assert result.count() == 2
    assert result.columns == columns