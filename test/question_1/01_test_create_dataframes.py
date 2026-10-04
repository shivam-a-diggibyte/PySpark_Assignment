def test_purchase_dataframe(spark):

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

    assert df.count() == 11
    assert df.columns == ["customer", "product_model"]


def test_product_dataframe(spark):

    data = [
        ("iphone13",),
        ("dell i5 core",),
        ("dell i3 core",),
        ("hp i5 core",),
        ("iphone14",)
    ]

    df = spark.createDataFrame(
        data,
        ["product_model"]
    )

    assert df.count() == 5
    assert df.columns == ["product_model"]