# PySpark Assignment

This repository contains the implementation of a PySpark assignment covering DataFrame creation, transformations, partition management, UDFs, JSON processing, joins, aggregations, and table operations.

The solutions are organized question-wise with separate test cases using `pytest` for better readability, maintainability, and validation.

## Repository Structure

```text
PySpark_Assignment/
├── src/
│   ├── Question_1/    # Customer & Product Analysis
│   ├── Question_2/    # Credit Card & Partitions
│   ├── Question_3/    # Login & User Activity
│   ├── Question_4/    # Nested JSON Processing
│   └── Question_5/    # Employee & Department Analysis
│
├── test/
│   ├── Question_1/
│   ├── Question_2/
│   ├── Question_3/
│   ├── Question_4/
│   └── Question_5/
│
├── README.md
└── .gitignore
```

## Topics Covered

- Custom schemas using `StructType` and `StructField`
- DataFrame transformations and filtering
- Customer and product analysis
- Partition management using `repartition()` and `coalesce()`
- User Defined Functions (UDFs)
- Credit card data masking
- Timestamp and date transformations
- CSV and JSON processing
- Nested JSON processing using `explode()`
- Dynamic column renaming
- Joins and aggregations
- Managed and external tables
- Pytest-based testing

## Testing

Run all tests:

```bash
pytest
```

Run tests for a specific question:

```bash
pytest test/Question_1/
pytest test/Question_2/
pytest test/Question_3/
pytest test/Question_4/
pytest test/Question_5/
```

## Purpose

The purpose of this repository is to demonstrate practical PySpark concepts through simple, modular implementations and automated tests.
