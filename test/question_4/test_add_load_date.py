from src.question_4.read_json import read_json_file
from src.question_4.flatten_json import flatten_employee_data
from src.question_4.add_load_date import add_load_date


def test_add_load_date(spark):

    file_path = "src/Question_4/employees.json"

    df = read_json_file(spark, file_path)

    flattened_df = flatten_employee_data(df)

    result_df = add_load_date(flattened_df)

    assert "load_date" in result_df.columns
    assert result_df.count() == 3