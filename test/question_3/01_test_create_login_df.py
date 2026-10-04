from pyspark.sql.types import StructType


def test_create_login_df(spark):
    data = [
        (1, 101, "login", "2023-09-05 08:30:00"),
        (2, 102, "click", "2023-09-06 12:45:00"),
        (3, 101, "click", "2023-09-07 14:15:00"),
        (4, 103, "login", "2023-09-08 09:00:00"),
        (5, 102, "logout", "2023-09-09 17:30:00"),
        (6, 101, "click", "2023-09-10 11:20:00"),
        (7, 103, "click", "2023-09-11 10:15:00"),
        (8, 102, "click", "2023-09-12 13:10:00")
    ]

    schema = StructType.fromJson({
        "type": "struct",
        "fields": [
            {"name": "log id", "type": "integer", "nullable": True, "metadata": {}},
            {"name": "user$id", "type": "integer", "nullable": True, "metadata": {}},
            {"name": "action", "type": "string", "nullable": True, "metadata": {}},
            {"name": "timestamp", "type": "string", "nullable": True, "metadata": {}}
        ]
    })

    df = spark.createDataFrame(data, schema)

    assert df.count() == 8
    assert df.columns == ["log id", "user$id", "action", "timestamp"]