from pyspark.sql.functions import collect_set, size, array_contains


def test_iphone13_only_customer(spark):

    data = [
        (1, "iphone13"),
        (1, "dell i5 core"),
        (2, "iphone13"),
        (2, "dell i5 core"),
        (3, "iphone13"),
        (3, "dell i5 core"),
        (1, "dell i3 core"),
        (1, "hp i5 core"),
        (1, "iphone14"),
        (3, "iphone14"),
        (4, "iphone13")
    ]

    df = spark.createDataFrame(
        data,
        ["customer", "product_model"]
    )

    result = (
        df.groupBy("customer")
        .agg(collect_set("product_model").alias("products"))
        .filter(
            (size("products") == 1) &
            array_contains("products", "iphone13")
        )
        .select("customer")
    )

    assert result.collect()[0]["customer"] == 4