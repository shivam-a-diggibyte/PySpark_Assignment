from src.question_5.create_dataframes import create_dataframes


def test_create_dataframes(spark):

    employee_df, department_df, country_df = create_dataframes(spark)

    assert employee_df.count() == 7
    assert department_df.count() == 5
    assert country_df.count() == 3

    assert employee_df.columns == [
        "employee_id",
        "employee_name",
        "department",
        "State",
        "salary",
        "Age"
    ]

    assert department_df.columns == [
        "dept_id",
        "dept_name"
    ]

    assert country_df.columns == [
        "country_code",
        "country_name"
    ]