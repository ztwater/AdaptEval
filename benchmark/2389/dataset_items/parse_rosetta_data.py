import sqlite3
import pandas as pd
from pandas.io.sql import SQLiteDatabase, SQLiteTable
import numpy as np
from tqdm import tqdm


def is_outlier(data, m=6.5):
            # https://stackoverflow.com/questions/11686720/is-there-a-numpy-builtin-to-reject-outliers-from-a-list
            d = np.abs(data - np.median(data))
            mdev = np.median(d)
            s = d / mdev if mdev else 0.
            return s > m

def df_to_sqlite(df: pd.DataFrame, db_file_name: str, table_name: str, chunk_size: int = 1_000_000):
    # https://stackoverflow.com/a/70488765/227755
    # https://stackoverflow.com/questions/56369565/large-6-million-rows-pandas-df-causes-memory-error-with-to-sql-when-chunksi
    con = sqlite3.connect(db_file_name)
    db = SQLiteDatabase(con=con)
    table = SQLiteTable(table_name, db, df, index=False, if_exists="append", dtype=None)
    table.create()
    insert = table.insert_statement(num_rows=1)  # single insert statement
    it = df.itertuples(index=False, name=None)  # just regular tuples
    pb = tqdm(it, total=len(df))  # not needed but nice to have
    with con:
        while True:
            con.execute("begin")
            try:
                for c in range(0, chunk_size):
                    row = next(it, None)
                    if row is None:
                        pb.update(c)
                        return
                    con.execute(insert, row)
                pb.update(chunk_size)
            finally:
                con.execute("commit")
