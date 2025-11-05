import pandas as pd
from pandas.io.sql import SQLiteDatabase, SQLiteTable
import sqlite3
from tqdm import tqdm

def df_to_sqlite(df: pd.DataFrame, db_file_name: str, table_name: str, chunk_size = 1_000_000):
    # see https://stackoverflow.com/a/70488765/227755
    con = sqlite3.connect(db_file_name)
    db = SQLiteDatabase(con=con)
    table = SQLiteTable(table_name, db, df, index=True, if_exists="fail", dtype=None)
    table.create()  # can be optimized further by postponing index creation, but that means we use private/protected APIs.
    insert = table.insert_statement(num_rows=1)  # single insert statement
    it = df.itertuples(index=True, name=None)  # just regular tuples
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
