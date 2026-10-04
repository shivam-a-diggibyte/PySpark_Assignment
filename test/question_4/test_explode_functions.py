from src.question_4.read_json import read_json_file
from src.question_4.explode_functions import (
    apply_explode,
    apply_explode_outer,
    apply_posexplode
)


def test_explode(spark):

    file_path = "src/Question_4/employees.json"

    df = read_json_file(spark, file_path)

    result_df = apply_explode(df)

    assert result_df.count() == 3


def test_explode_outer(spark):

    file_path = "src/Question_4/employees.json"

    df = read_json_file(spark, file_path)

    result_df = apply_explode_outer(df)

    assert result_df.count() == 3


def test_posexplode(spark):

    file_path = "src/Question_4/employees.json"

    df = read_json_file(spark, file_path)

    result_df = apply_posexplode(df)

    assert result_df.count() == 3
    assert result_df.columns == ["id", "position", "employee"]