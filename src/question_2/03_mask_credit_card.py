from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql.functions import udf


spark = (
    SparkSession.builder
    .appName("Mask Credit Card")
    .master("local[*]")
    .getOrCreate()
)

# Data
data = [
    ("1234567891234567",),
    ("5678912345671234",),
    ("9123456712345678",),
    ("1234567812341122",),
    ("1234567812341342",)
]

# Schema
schema = StructType([
    StructField("card_number", StringType(), True)
])

# Create DataFrame
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

result_df.show(truncate=False)


spark.stop()