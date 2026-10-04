from pyspark.sql.types import StructType, StructField, StringType


def test_create_credit_card_df(spark):
    data = [
        ("1234567891234567",),
        ("5678912345671234",),
        ("9123456712345678",),
        ("1234567812341122",),
        ("1234567812341342",)
    ]

    schema = StructType([
        StructField("card_number", StringType(), True)
    ])

    credit_card_df = spark.createDataFrame(data, schema)

    # Check number of records
    assert credit_card_df.count() == 5

    # Check column name
    assert credit_card_df.columns == ["card_number"]

    # Check schema
    assert isinstance(credit_card_df.schema, StructType)

    # Check first card number
    assert credit_card_df.first()["card_number"] == "1234567891234567"