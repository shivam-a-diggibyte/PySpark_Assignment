from src.question_5.create_dataframes import create_dataframes
from src.question_5.average_salary import calculate_average_salary


def test_average_salary(spark):

    employee_df, _, _ = create_dataframes(spark)

    result_df = calculate_average_salary(employee_df)

    assert result_df.count() == 3

    departments = {
        row["department"]
        for row in result_df.collect()
    }

    assert departments == {"D101", "D102", "D103"}