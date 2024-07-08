import sys

from pyspark.sql import DataFrame, SparkSession


def extract(spark: SparkSession, input_path: str) -> DataFrame:
    # TODO load
    return None


def transform(df: DataFrame) -> DataFrame:
    # TODO transformation

    return df


def load(df: DataFrame, output_path: str) -> None:
    # TODO

    return None


def run_pipeline(spark: SparkSession,
                 input_path: str,
                 output_path: str) -> None:

    df = extract(spark, input_path)
    df = transform(df)
    load(df, output_path)


def main():
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    spark = SparkSession.builder \
        .enableHiveSupport() \
        .getOrCreate()

    run_pipeline(spark, input_path, output_path)


if __name__ == '__main__':
    main()
