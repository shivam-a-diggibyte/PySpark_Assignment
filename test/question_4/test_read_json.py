from src.question_4.read_json import read_json_file


def test_read_json(spark):

    file_path = "src/Question_4/employees.json"

    df = read_json_file(spark, file_path)

    assert df.count() == 1
    assert df.columns == ["id", "properties", "employees"]