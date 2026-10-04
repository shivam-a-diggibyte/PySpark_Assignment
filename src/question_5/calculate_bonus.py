from pyspark.sql.functions import col


def calculate_bonus(employee_df):

    return employee_df.withColumn(
        "bonus",
        col("salary") * 2
    )


if __name__ == "__main__":

    from pyspark.sql import SparkSession
    from create_dataframes import create_dataframes

    spark = (
        SparkSession.builder
        .appName("Question_5_Bonus")
        .master("local[*]")
        .getOrCreate()
    )

    employee_df, _, _ = create_dataframes(spark)

    result_df = calculate_bonus(employee_df)

    result_df.show()

    spark.stop()