from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import IntegerType, StringType


spark = (
    SparkSession.builder
    .appName("Question 1")
    .master("local[*]")
    .getOrCreate()
)


purchase_data = [
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

purchase_schema = StructType([
    StructField("customer", IntegerType(), True),
    StructField("product_model", StringType(), True)
])

purchase_data_df = spark.createDataFrame(
    purchase_data,
    purchase_schema
)


product_data = [
    ("iphone13",),
    ("dell i5 core",),
    ("dell i3 core",),
    ("hp i5 core",),
    ("iphone14",)
]

product_schema = StructType([
    StructField("product_model", StringType(), True)
])

product_data_df = spark.createDataFrame(
    product_data,
    product_schema
)


purchase_data_df.show()
product_data_df.show()

spark.stop()