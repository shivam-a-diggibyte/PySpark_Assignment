from src.question_4.read_json import read_json_file
from src.question_4.flatten_json import flatten_employee_data
from src.question_4.add_load_date import add_load_date
from src.question_4.create_date_columns import create_date_columns
from src.question_4.write_employee_table import write_employee_table


def test_write_employee_table(spark):

    file_path = "src/Question_4/employees.json"

    df = read_json_file(spark, file_path)

    df = flatten_employee_data(df)
    df = add_load_date(df)
    df = create_date_columns(df)

    write_employee_table(df, spark)

    result_df = spark.table("employee.employee_details")

    assert result_df.count() == 3