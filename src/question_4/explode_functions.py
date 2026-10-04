from pyspark.sql.functions import (
    explode,
    explode_outer,
    posexplode
)


def apply_explode(employee_df):

    return employee_df.select(
        "id",
        explode("employees").alias("employee")
    )


def apply_explode_outer(employee_df):

    return employee_df.select(
        "id",
        explode_outer("employees").alias("employee")
    )


def apply_posexplode(employee_df):

    return employee_df.select(
        "id",
        posexplode("employees").alias("position", "employee")
    )


if __name__ == "__main__":

    from pyspark.sql import SparkSession
    from read_json import read_json_file

    spark = (
        SparkSession.builder
        .appName("Question_4_Explode_Functions")
        .master("local[*]")
        .getOrCreate()
    )

    file_path = "src/Question_4/employees.json"

    employee_df = read_json_file(spark, file_path)

    print("explode:")
    apply_explode(employee_df).show()

    print("explode_outer:")
    apply_explode_outer(employee_df).show()

    print("posexplode:")
    apply_posexplode(employee_df).show()

    spark.stop()