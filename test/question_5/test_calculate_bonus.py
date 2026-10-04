from src.question_5.create_dataframes import create_dataframes
from src.question_5.calculate_bonus import calculate_bonus


def test_calculate_bonus(spark):

    employee_df, _, _ = create_dataframes(spark)

    result_df = calculate_bonus(employee_df)

    assert "bonus" in result_df.columns

    first_row = result_df.filter(
        result_df.employee_id == 11
    ).first()

    assert first_row["bonus"] == 18000