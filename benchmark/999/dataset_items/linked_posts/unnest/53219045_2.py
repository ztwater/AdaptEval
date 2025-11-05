vals = df.B.values.tolist()
rs = [len(r) for r in vals]    
a = np.repeat(df.A, rs)

pd.DataFrame(np.column_stack((a, np.concatenate(vals))), columns=df.columns)
