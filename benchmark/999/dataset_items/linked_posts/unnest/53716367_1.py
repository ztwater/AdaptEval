df[['B1', 'B2']] = pd.DataFrame([*df['B']]) # if values.tolist() is too boring

(pd.wide_to_long(df.drop('B', 1), 'B', 'A', '')
 .reset_index(level=1, drop=True)
 .reset_index())
