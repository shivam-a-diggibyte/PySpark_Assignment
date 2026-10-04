from src.question_5.create_dataframes import create_dataframes
from src.question_5.dynamic_joins import dynamic_join


def test_inner_join(spark):

    employee_df, department_df, _ = create_dataframes(spark)

    result_df = dynamic_join(
        employee_df,
        department_df,
        "inner"
    )

    assert result_df.count() == 7


def test_left_join(spark):

    employee_df, department_df, _ = create_dataframes(spark)

    result_df = dynamic_join(
        employee_df,
        department_df,
        "left"
    )

    assert result_df.count() == 7


def test_right_join(spark):

    employee_df, department_df, _ = create_dataframes(spark)

    result_df = dynamic_join(
        employee_df,
        department_df,
        "right"
    )

    assert result_df.count() == 5