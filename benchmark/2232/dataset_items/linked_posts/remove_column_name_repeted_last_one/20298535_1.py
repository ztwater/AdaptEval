def drop_col_n(df, col_n_to_drop):
    col_dict = {x: col for x, col in enumerate(df.columns)}
    return df.drop(col_dict[col_n_to_drop], 1)

df = drop_col_n(df, 2)
