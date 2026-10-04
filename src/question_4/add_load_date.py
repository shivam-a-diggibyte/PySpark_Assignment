from pyspark.sql.functions import current_date


def add_load_date(df):

    return df.withColumn(
        "load_date",
        current_date()
    )


if __name__ == "__main__":

    from pyspark.sql import SparkSession
    from read_json import read_json_file
    from flatten_json import flatten_employee_data

    spark = (
        SparkSession.builder
        .appName("Question_4_Load_Date")
        .master("local[*]")
        .getOrCreate()
    )

    file_path = "src/Question_4/employees.json"

    employee_df = read_json_file(spark, file_path)

    flattened_df = flatten_employee_data(employee_df)

    result_df = add_load_date(flattened_df)

    result_df.show()

    spark.stop()