def reorder_employee_columns(employee_df):

    return employee_df.select(
        "employee_id",
        "employee_name",
        "salary",
        "State",
        "Age",
        "department"
    )


if __name__ == "__main__":

    from pyspark.sql import SparkSession
    from create_dataframes import create_dataframes

    spark = (
        SparkSession.builder
        .appName("Question_5_Reorder_Columns")
        .master("local[*]")
        .getOrCreate()
    )

    employee_df, _, _ = create_dataframes(spark)

    result_df = reorder_employee_columns(employee_df)

    result_df.show()

    spark.stop()