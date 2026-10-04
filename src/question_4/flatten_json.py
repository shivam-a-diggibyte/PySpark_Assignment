from pyspark.sql.functions import explode

from question_4 import read_json


def flatten_employee_data(employee_df):

    flattened_df = employee_df.select(
        "id",
        "properties.name",
        "properties.storeSize",
        explode("employees").alias("employee")
    )

    flattened_df = flattened_df.select(
        "id",
        "name",
        "storeSize",
        "employee.empId",
        "employee.empName"
    )

    return flattened_df

if __name__ == "__main__":

    from pyspark.sql import SparkSession
    from read_json import read_json_file

    spark = (
        SparkSession.builder
        .appName("Question_4_Flatten_JSON")
        .master("local[*]")
        .getOrCreate()
    )

    file_path = "src/Question_4/employees.json"

    employee_df = read_json_file(spark, file_path)

    flattened_df = flatten_employee_data(employee_df)

    flattened_df.show()

    spark.stop()