from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType


spark = (
    SparkSession.builder
    .appName("Partition Operations")
    .master("local[*]")
    .getOrCreate()
)

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


# Original number of partitions
original_partitions = credit_card_df.rdd.getNumPartitions()

print("Original partitions:", original_partitions)


# Increase partitions to 5
credit_card_df = credit_card_df.repartition(5)

print("After increasing:", credit_card_df.rdd.getNumPartitions())


# Decrease back to original number
credit_card_df = credit_card_df.coalesce(original_partitions)

print("After decreasing:", credit_card_df.rdd.getNumPartitions())


spark.stop()