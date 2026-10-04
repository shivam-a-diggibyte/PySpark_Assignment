def create_external_tables(
    employee_df,
    spark,
    parquet_path,
    csv_path
):

    spark.sql("CREATE DATABASE IF NOT EXISTS employee")

    (
        employee_df.write
        .mode("overwrite")
        .format("parquet")
        .option("path", parquet_path)
        .saveAsTable("employee.employee_parquet")
    )

    (
        employee_df.write
        .mode("overwrite")
        .format("csv")
        .option("header", True)
        .option("path", csv_path)
        .saveAsTable("employee.employee_csv")
    )


if __name__ == "__main__":

    from pyspark.sql import SparkSession
    from create_dataframes import create_dataframes

    spark = (
        SparkSession.builder
        .appName("Question_5_External_Tables")
        .master("local[*]")
        .getOrCreate()
    )

    employee_df, _, _ = create_dataframes(spark)

    create_external_tables(
        employee_df,
        spark,
        "output/employee_parquet",
        "output/employee_csv"
    )

    print("External tables created successfully.")

    spark.stop()