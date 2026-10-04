from pyspark.sql.functions import col


def employees_starting_with_m(employee_df, department_df):

    joined_df = employee_df.join(
        department_df,
        employee_df.department == department_df.dept_id,
        "inner"
    )

    return joined_df.filter(
        col("employee_name").startswith("m")
    ).select(
        "employee_name",
        "dept_name"
    )


if __name__ == "__main__":

    from pyspark.sql import SparkSession
    from create_dataframes import create_dataframes

    spark = (
        SparkSession.builder
        .appName("Question_5_Employees_M")
        .master("local[*]")
        .getOrCreate()
    )

    employee_df, department_df, _ = create_dataframes(spark)

    result_df = employees_starting_with_m(
        employee_df,
        department_df
    )

    result_df.show()

    spark.stop()