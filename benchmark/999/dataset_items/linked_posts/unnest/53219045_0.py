vals = np.array(df.B.values.tolist())    
a = np.repeat(df.A, vals.shape[1])

pd.DataFrame(np.column_stack((a, vals.ravel())), columns=df.columns)
