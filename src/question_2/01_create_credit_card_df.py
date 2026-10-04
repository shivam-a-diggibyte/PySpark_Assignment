from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType


spark = (
    SparkSession.builder
    .appName("Credit Card Data")
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

# Custom schema
schema = StructType([
    StructField("card_number", StringType(), True)
])

# Create DataFrame
credit_card_df = spark.createDataFrame(data, schema)

credit_card_df.show()

spark.stop()