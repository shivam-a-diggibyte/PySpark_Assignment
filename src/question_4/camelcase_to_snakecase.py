import re


def camel_to_snake(column_name):

    return re.sub(
        r'(?<!^)(?=[A-Z])',
        '_',
        column_name
    ).lower()


def convert_columns_to_snake_case(df):

    for column_name in df.columns:

        new_column_name = camel_to_snake(column_name)

        df = df.withColumnRenamed(
            column_name,
            new_column_name
        )

    return df


if __name__ == "__main__":

    from pyspark.sql import SparkSession
    from read_json import read_json_file
    from flatten_json import flatten_employee_data

    spark = (
        SparkSession.builder
        .appName("Question_4_Snake_Case")
        .master("local[*]")
        .getOrCreate()
    )

    file_path = "src/Question_4/employees.json"

    employee_df = read_json_file(spark, file_path)

    flattened_df = flatten_employee_data(employee_df)

    result_df = convert_columns_to_snake_case(flattened_df)

    result_df.show()

    spark.stop()