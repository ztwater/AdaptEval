def get_data_by_chunks(cls, table, chunksize: int) -> iter:
    with MysqlClient.get_engine().begin() as conn:
        query_count = "select COUNT(*) from my_query"
        row_count = conn.execute(query_count, where).fetchone()[0]

        for i in range(math.ceil(row_count / chunksize)):
            query = """
               SELECT * FROM my_table
               WHERE my_filiters
               LIMIT {offset}, {row_count};
             """
            yield pd.read_sql(query, conn)

for df in get_data_by_chunks(cls, table, chunksize: int):
    print(df.shape)
