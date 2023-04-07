import pandas as pd
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, DateType, TimestampType
from clean.load import Load
from clean.transform import Transform

import pyspark
import pyspark.pandas as ps
from pyspark.sql import SparkSession


def save(df: pd.DataFrame):
    spark = SparkSession.builder.appName('PySpark').getOrCreate()

    schema = StructType(
        [StructField("year_month", DateType(), True),
         StructField("uf", StringType(), True),
         StructField("product", StringType(), True),
         StructField("unit", StringType(), True),
         StructField("volume", DoubleType(), True),
         StructField("created_at", TimestampType(), True),
         ])
    sp_df = spark.createDataFrame(df, schema=schema)

    sp_df.write.option("header", True) \
        .partitionBy("year_month") \
        .mode("overwrite") \
        .parquet("vendas_y.parquet")


