import pandas as pd
import datetime as dt


class Transform:
    def __init__(self):
        self.dfs = []

    def add_raw_df(self, raw_df: pd.DataFrame):
        self.dfs.append(self._transform(raw_df))

    def get_final_table(self) -> pd.DataFrame:
        return pd.concat(self.dfs, ignore_index=True)


    def _transform(self, table: pd.DataFrame) -> pd.DataFrame:

        # unit of every product (hardcoded)
        unit = 'm3'

        # listing mapping brazilian months to integers
        months = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
        months_to_int_d = {m: i for m, i in zip(months, range(1, 12 + 1))}
        months_to_int = lambda x: months_to_int_d[x]

        # transforming the data
        table = table.melt(id_vars=['ANO', 'COMBUSTÍVEL', 'ESTADO'],
                           value_vars=months, var_name='MONTH',
                           value_name='volume')
        table['month_int'] = table.apply(lambda x: months_to_int(x['MONTH']), axis=1)
        table['year_month'] = table.apply(lambda x: dt.datetime(x['ANO'], x['month_int'], 1), axis=1)
        table.rename({'COMBUSTÍVEL': 'product', 'ESTADO': 'uf'}, inplace=True, axis=1)
        table['unit'] = unit
        table['created_at'] = pd.Timestamp.now()
        table = table[['year_month', 'uf', 'product', 'unit', 'volume', 'created_at']]

        return table


