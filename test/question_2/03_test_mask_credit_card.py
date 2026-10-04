from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql.functions import udf


def test_mask_credit_card(spark):

    data = [
        ("1234567891234567",),
        ("5678912345671234",),
        ("9123456712345678",)
    ]

    schema = StructType([
        StructField("card_number", StringType(), True)
    ])

    credit_card_df = spark.createDataFrame(data, schema)

    # Masking function
    def mask_card_number(card_number):
        return "*" * (len(card_number) - 4) + card_number[-4:]

    # Create UDF
    mask_udf = udf(mask_card_number, StringType())

    # Apply UDF
    result_df = credit_card_df.withColumn(
        "masked_card_number",
        mask_udf("card_number")
    )

    result = result_df.collect()

    # Check masked values
    assert result[0]["masked_card_number"] == "************4567"
    assert result[1]["masked_card_number"] == "************1234"
    assert result[2]["masked_card_number"] == "************5678"

    # Check column names
    assert result_df.columns == [
        "card_number",
        "masked_card_number"
    ]