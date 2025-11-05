columns_list = [1, 2, 4] # index numbers of columns you want to delete
df = df.drop(columns=df.columns[columns_list])
