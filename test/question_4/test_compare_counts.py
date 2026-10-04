from src.question_4.read_json import read_json_file
from src.question_4.compare_counts import compare_record_counts


def test_compare_counts(spark):

    file_path = "src/Question_4/employees.json"

    df = read_json_file(spark, file_path)

    non_flattened_count, flattened_count = compare_record_counts(df)

    assert non_flattened_count == 1
    assert flattened_count == 3