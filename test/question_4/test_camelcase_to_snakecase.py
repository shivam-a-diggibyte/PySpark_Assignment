from src.question_4.read_json import read_json_file
from src.question_4.flatten_json import flatten_employee_data
from src.question_4.camelcase_to_snakecase import (
    camel_to_snake,
    convert_columns_to_snake_case
)


def test_camel_to_snake():

    assert camel_to_snake("storeSize") == "store_size"
    assert camel_to_snake("empId") == "emp_id"
    assert camel_to_snake("empName") == "emp_name"


def test_convert_columns_to_snake_case(spark):

    file_path = "src/Question_4/employees.json"

    df = read_json_file(spark, file_path)

    flattened_df = flatten_employee_data(df)

    result_df = convert_columns_to_snake_case(flattened_df)

    assert result_df.columns == [
        "id",
        "name",
        "store_size",
        "emp_id",
        "emp_name"
    ]