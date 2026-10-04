from src.question_5.create_dataframes import create_dataframes
from src.question_5.replace_state_with_country import (
    replace_state_with_country
)


def test_replace_state_with_country(spark):

    employee_df, _, country_df = create_dataframes(spark)

    result_df = replace_state_with_country(
        employee_df,
        country_df
    )

    assert result_df.count() == 7

    assert "State" in result_df.columns

    states = {
        row["State"]
        for row in result_df.collect()
    }

    assert states == {
        "newyork",
        "California",
        "Russia"
    }