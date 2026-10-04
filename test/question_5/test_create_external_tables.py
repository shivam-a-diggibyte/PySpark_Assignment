from src.question_5.create_dataframes import create_dataframes
from src.question_5.create_external_tables import (
    create_external_tables
)


def test_create_external_tables(spark, tmp_path):

    employee_df, _, _ = create_dataframes(spark)

    parquet_path = str(tmp_path / "employee_parquet")
    csv_path = str(tmp_path / "employee_csv")

    create_external_tables(
        employee_df,
        spark,
        parquet_path,
        csv_path
    )

    parquet_df = spark.table(
        "employee.employee_parquet"
    )

    csv_df = spark.table(
        "employee.employee_csv"
    )

    assert parquet_df.count() == 7
    assert csv_df.count() == 7