from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType
)


employee_schema = StructType([
    StructField("employee_id", IntegerType(), True),
    StructField("employee_name", StringType(), True),
    StructField("department", StringType(), True),
    StructField("State", StringType(), True),
    StructField("salary", IntegerType(), True),
    StructField("Age", IntegerType(), True)
])


department_schema = StructType([
    StructField("dept_id", StringType(), True),
    StructField("dept_name", StringType(), True)
])


country_schema = StructType([
    StructField("country_code", StringType(), True),
    StructField("country_name", StringType(), True)
])


def create_dataframes(spark):

    employee_data = [
        (11, "james", "D101", "ny", 9000, 34),
        (12, "michel", "D101", "ny", 8900, 32),
        (13, "robert", "D102", "ca", 7900, 29),
        (14, "scott", "D103", "ca", 8000, 36),
        (15, "jen", "D102", "ny", 9500, 38),
        (16, "jeff", "D103", "uk", 9100, 35),
        (17, "maria", "D101", "ny", 7900, 40)
    ]

    department_data = [
        ("D101", "sales"),
        ("D102", "finance"),
        ("D103", "marketing"),
        ("D104", "hr"),
        ("D105", "support")
    ]

    country_data = [
        ("ny", "newyork"),
        ("ca", "California"),
        ("uk", "Russia")
    ]

    employee_df = spark.createDataFrame(
        employee_data,
        employee_schema
    )

    department_df = spark.createDataFrame(
        department_data,
        department_schema
    )

    country_df = spark.createDataFrame(
        country_data,
        country_schema
    )

    return employee_df, department_df, country_df


if __name__ == "__main__":

    spark = (
        SparkSession.builder
        .appName("Question_5_Create_DataFrames")
        .master("local[*]")
        .getOrCreate()
    )

    employee_df, department_df, country_df = create_dataframes(spark)

    employee_df.show()
    department_df.show()
    country_df.show()

    spark.stop()