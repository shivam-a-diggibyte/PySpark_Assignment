from src.question_5.create_dataframes import create_dataframes
from src.question_5.reorder_columns import reorder_employee_columns


def test_reorder_columns(spark):

    employee_df, _, _ = create_dataframes(spark)

    result_df = reorder_employee_columns(employee_df)

    assert result_df.columns == [
        "employee_id",
        "employee_name",
        "salary",
        "State",
        "Age",
        "department"
    ]