from src.question_5.create_dataframes import create_dataframes
from src.question_5.employees_name_m import employees_starting_with_m


def test_employees_starting_with_m(spark):

    employee_df, department_df, _ = create_dataframes(spark)

    result_df = employees_starting_with_m(
        employee_df,
        department_df
    )

    assert result_df.count() == 2

    employee_names = {
        row["employee_name"]
        for row in result_df.collect()
    }

    assert employee_names == {"michel", "maria"}