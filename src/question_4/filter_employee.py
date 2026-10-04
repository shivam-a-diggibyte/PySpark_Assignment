from pyspark.sql.functions import col


def filter_employee(employee_df):

    return employee_df.filter(col("id") == 1001)


if __name__ == "__main__":

    from pyspark.sql import SparkSession
    from read_json import read_json_file

    spark = (
        SparkSession.builder
        .appName("Question_4_Filter_Employee")
        .master("local[*]")
        .getOrCreate()
    )

    file_path = "src/Question_4/employees.json"

    employee_df = read_json_file(spark, file_path)

    filtered_df = filter_employee(employee_df)

    filtered_df.show(truncate=False)

    spark.stop()