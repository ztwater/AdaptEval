df = df.iloc[:, [j for j, c in enumerate(df.columns) if j != i]]
