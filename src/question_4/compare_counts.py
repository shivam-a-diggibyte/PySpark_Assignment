from pyspark.sql.functions import explode


def compare_record_counts(employee_df):

    non_flattened_count = employee_df.count()

    flattened_df = employee_df.select(
        "id",
        explode("employees").alias("employee")
    )

    flattened_count = flattened_df.count()

    return non_flattened_count, flattened_count


if __name__ == "__main__":

    from pyspark.sql import SparkSession
    from read_json import read_json_file

    spark = (
        SparkSession.builder
        .appName("Question_4_Compare_Counts")
        .master("local[*]")
        .getOrCreate()
    )

    file_path = "src/Question_4/employees.json"

    employee_df = read_json_file(spark, file_path)

    non_flattened_count, flattened_count = compare_record_counts(
        employee_df
    )

    print("Non-flattened count:", non_flattened_count)
    print("Flattened count:", flattened_count)

    spark.stop()