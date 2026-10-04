from pyspark.sql.functions import (
    year,
    month,
    dayofmonth
)


def create_date_columns(df):

    return (
        df.withColumn("year", year("load_date"))
          .withColumn("month", month("load_date"))
          .withColumn("day", dayofmonth("load_date"))
    )


if __name__ == "__main__":

    from pyspark.sql import SparkSession
    from read_json import read_json_file
    from flatten_json import flatten_employee_data
    from add_load_date import add_load_date

    spark = (
        SparkSession.builder
        .appName("Question_4_Date_Columns")
        .master("local[*]")
        .getOrCreate()
    )

    file_path = "src/Question_4/employees.json"

    employee_df = read_json_file(spark, file_path)

    flattened_df = flatten_employee_data(employee_df)

    df = add_load_date(flattened_df)

    result_df = create_date_columns(df)

    result_df.show()

    spark.stop()