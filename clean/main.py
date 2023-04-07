import pandas as pd
from pyspark.sql.types import StructType,StructField, StringType, DoubleType, DateType, TimestampType
from clean.load import Load
from clean.transform import Transform
from save import save

if __name__ == '__main__':

    load = Load()

    dfs = load.load_all()

    t = Transform()

    for df in dfs:
        t.add_raw_df(df)

    df = t.get_final_table()

    save(df)

