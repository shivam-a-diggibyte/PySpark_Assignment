from src.question_4.read_json import read_json_file
from src.question_4.flatten_json import flatten_employee_data
from src.question_4.add_load_date import add_load_date
from src.question_4.create_date_columns import create_date_columns


def test_create_date_columns(spark):

    file_path = "src/Question_4/employees.json"

    df = read_json_file(spark, file_path)

    flattened_df = flatten_employee_data(df)

    df = add_load_date(flattened_df)

    result_df = create_date_columns(df)

    assert "year" in result_df.columns
    assert "month" in result_df.columns
    assert "day" in result_df.columns

    assert result_df.count() == 3