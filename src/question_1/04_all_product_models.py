from pyspark.sql import SparkSession
from pyspark.sql.functions import countDistinct


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

product_data = [
    ("iphone13",),
    ("dell i5 core",),
    ("dell i3 core",),
    ("hp i5 core",),
    ("iphone14",)
]


purchase_df = spark.createDataFrame(
    purchase_data,
    ["customer", "product_model"]
)

product_df = spark.createDataFrame(
    product_data,
    ["product_model"]
)


total_products = product_df.count()

result = (
    purchase_df
    .groupBy("customer")
    .agg(countDistinct("product_model").alias("product_count"))
    .filter("product_count = " + str(total_products))
    .select("customer")
)


result.show()

spark.stop()