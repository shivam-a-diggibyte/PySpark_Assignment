def dynamic_join(employee_df, department_df, join_type):

    return employee_df.join(
        department_df,
        employee_df.department == department_df.dept_id,
        join_type
    )


if __name__ == "__main__":

    from pyspark.sql import SparkSession
    from create_dataframes import create_dataframes

    spark = (
        SparkSession.builder
        .appName("Question_5_Dynamic_Joins")
        .master("local[*]")
        .getOrCreate()
    )

    employee_df, department_df, _ = create_dataframes(spark)

    inner_df = dynamic_join(
        employee_df,
        department_df,
        "inner"
    )

    left_df = dynamic_join(
        employee_df,
        department_df,
        "left"
    )

    right_df = dynamic_join(
        employee_df,
        department_df,
        "right"
    )

    print("INNER JOIN")
    inner_df.show()

    print("LEFT JOIN")
    left_df.show()

    print("RIGHT JOIN")
    right_df.show()

    spark.stop()