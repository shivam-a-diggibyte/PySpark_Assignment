from src.question_4.read_json import read_json_file
from src.question_4.flatten_json import flatten_employee_data


def test_flatten_json(spark):

    file_path = "src/Question_4/employees.json"

    df = read_json_file(spark, file_path)

    result_df = flatten_employee_data(df)

    assert result_df.count() == 3

    assert result_df.columns == [
        "id",
        "name",
        "storeSize",
        "empId",
        "empName"
    ]