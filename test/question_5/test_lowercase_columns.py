from src.question_5.create_dataframes import create_dataframes
from src.question_5.lowercase_columns import lowercase_columns


def test_lowercase_columns(spark):

    employee_df, _, _ = create_dataframes(spark)

    result_df = lowercase_columns(employee_df)

    assert result_df.columns == [
        "employee_id",
        "employee_name",
        "department",
        "state",
        "salary",
        "age",
        "load_date"
    ]

    assert result_df.count() == 7