def write_employee_table(df, spark):

    spark.sql("CREATE DATABASE IF NOT EXISTS employee")

    (
        df.write
        .format("json")
        .mode("overwrite")
        .partitionBy("year", "month", "day")
        .saveAsTable("employee.employee_details")
    )


if __name__ == "__main__":

    from pyspark.sql import SparkSession

    from read_json import read_json_file
    from flatten_json import flatten_employee_data
    from add_load_date import add_load_date
    from create_date_columns import create_date_columns

    spark = (
        SparkSession.builder
        .appName("Question_4_Write_Employee_Table")
        .master("local[*]")
        .getOrCreate()
    )

    file_path = "src/Question_4/employees.json"

    employee_df = read_json_file(spark, file_path)

    flattened_df = flatten_employee_data(employee_df)

    df = add_load_date(flattened_df)

    df = create_date_columns(df)

    write_employee_table(df, spark)

    print("employee.employee_details table created successfully.")

    spark.stop()