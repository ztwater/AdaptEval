import pandas as pd
from pandas.io.sql import SQLiteDatabase, SQLiteTable
import sqlite3
from tqdm import tqdm

def df_to_sqlite(var_0: pd.DataFrame, var_1: str, var_2: str, var_3 = 1_000_000):
    # see https://stackoverflow.com/a/70488765/227755
    var_4 = sqlite3.connect(var_1)
    var_5 = SQLiteDatabase(var_4=var_4)
    var_6 = SQLiteTable(var_2, var_5, var_0, index=True, if_exists="fail", dtype=None)
    var_6.create()  # can be optimized further by postponing index creation, but that means we use private/protected APIs.
    var_7 = var_6.insert_statement(num_rows=1)  # single insert statement
    var_8 = var_0.itertuples(index=True, name=None)  # just regular tuples
    var_9 = tqdm(var_8, total=len(var_0))  # not needed but nice to have
    with var_4:
        while True:
            var_4.execute("begin")
            try:
                for c in range(0, var_3):
                    var_10 = next(var_8, None)
                    if var_10 is None:
                        var_9.update(c)
                        return
                    var_4.execute(var_7, var_10)
                var_9.update(var_3)
            finally:
                var_4.execute("commit")
