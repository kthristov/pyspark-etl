import os

import pytest
from pyspark.sql import SparkSession
from pyspark.testing.utils import assertDataFrameEqual

from src.main import transform


@pytest.fixture(scope='session')
def spark():
    spark =  SparkSession.builder.appName('test_session').getOrCreate()
    yield spark


def test_sample(spark):
    sample_data = [
        {"name": "John D.", "age": 30},
        {"name": "Alice G.", "age": 25},
        {"name": "Bob T.", "age": 35},
        {"name": "Eve A.", "age": 28}]

    # Create a Spark DataFrame
    original_df = spark.createDataFrame(sample_data)

    expected_data = [
        {"name": "Bob T.", "age": 35},
        {"name": "Eve A.", "age": 28},
        {"name": "John D.", "age": 30},
        {"name": "Alice G.", "age": 25},]

    expected_df = spark.createDataFrame(expected_data)

    assertDataFrameEqual(original_df, expected_df)


def test_transform(spark):
    input_path = os.path.join(os.path.dirname(__file__), 'data', 'walmart_producs_sample.jsonl.gz')

    # To be provided 
    expected_output_path = os.path.join(os.path.dirname(__file__), 'data', 'expected_output.csv')

    input_df = spark.read.json(input_path)
    transformed_df = transform(input_df)
    expected_df = spark.read.csv(expected_output_path, header=True, inferSchema=True)

    # Compare the output data with the expected data
    assertDataFrameEqual(transformed_df, expected_df)
