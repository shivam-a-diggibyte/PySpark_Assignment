from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType,
    ArrayType
)


employee_schema = StructType([
    StructField("id", IntegerType(), True),

    StructField(
        "properties",
        StructType([
            StructField("name", StringType(), True),
            StructField("storeSize", StringType(), True)
        ]),
        True
    ),

    StructField(
        "employees",
        ArrayType(
            StructType([
                StructField("empId", IntegerType(), True),
                StructField("empName", StringType(), True)
            ])
        ),
        True
    )
])


def read_json_file(spark, file_path):
    return spark.read.schema(employee_schema).json(file_path)


if __name__ == "__main__":

    spark = (
        SparkSession.builder
        .appName("Question_4_Read_JSON")
        .master("local[*]")
        .getOrCreate()
    )

    file_path = "src/Question_4/employees.json"

    employee_df = read_json_file(spark, file_path)

    employee_df.show(truncate=False)

    employee_df.printSchema()

    spark.stop()