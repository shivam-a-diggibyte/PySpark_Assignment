def replace_state_with_country(employee_df, country_df):

    return (
        employee_df
        .join(
            country_df,
            employee_df.State == country_df.country_code,
            "left"
        )
        .select(
            employee_df.employee_id,
            employee_df.employee_name,
            employee_df.department,
            country_df.country_name.alias("State"),
            employee_df.salary,
            employee_df.Age
        )
    )


if __name__ == "__main__":

    from pyspark.sql import SparkSession
    from create_dataframes import create_dataframes

    spark = (
        SparkSession.builder
        .appName("Question_5_Country")
        .master("local[*]")
        .getOrCreate()
    )

    employee_df, _, country_df = create_dataframes(spark)

    result_df = replace_state_with_country(
        employee_df,
        country_df
    )

    result_df.show()

    spark.stop()