from pyspark.sql.functions import avg


def calculate_average_salary(employee_df):

    return (
        employee_df
        .groupBy("department")
        .agg(
            avg("salary").alias("average_salary")
        )
    )


if __name__ == "__main__":

    from pyspark.sql import SparkSession
    from create_dataframes import create_dataframes

    spark = (
        SparkSession.builder
        .appName("Question_5_Average_Salary")
        .master("local[*]")
        .getOrCreate()
    )

    employee_df, _, _ = create_dataframes(spark)

    result_df = calculate_average_salary(employee_df)

    result_df.show()

    spark.stop()