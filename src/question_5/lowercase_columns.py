from pyspark.sql.functions import current_date


def lowercase_columns(df):

    for column_name in df.columns:
        df = df.withColumnRenamed(
            column_name,
            column_name.lower()
        )

    df = df.withColumn(
        "load_date",
        current_date()
    )

    return df


if __name__ == "__main__":

    from pyspark.sql import SparkSession
    from create_dataframes import create_dataframes

    spark = (
        SparkSession.builder
        .appName("Question_5_Lowercase")
        .master("local[*]")
        .getOrCreate()
    )

    employee_df, _, _ = create_dataframes(spark)

    result_df = lowercase_columns(employee_df)

    result_df.show()
    result_df.printSchema()

    spark.stop()