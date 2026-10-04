from src.question_4.read_json import read_json_file
from src.question_4.filter_employee import filter_employee


def test_filter_employee(spark):

    file_path = "src/Question_4/employees.json"

    df = read_json_file(spark, file_path)

    result_df = filter_employee(df)

    assert result_df.count() == 1
    assert result_df.first()["id"] == 1001