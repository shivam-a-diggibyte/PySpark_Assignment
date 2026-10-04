from pyspark.sql.types import StructType, StructField, StringType


def test_partition_operations(spark):
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

    # Original partitions
    original_partitions = credit_card_df.rdd.getNumPartitions()

    assert original_partitions > 0

    # Increase to 5
    credit_card_df = credit_card_df.repartition(5)

    assert credit_card_df.rdd.getNumPartitions() == 5

    # Decrease back to original
    credit_card_df = credit_card_df.coalesce(original_partitions)

    assert credit_card_df.rdd.getNumPartitions() == original_partitions