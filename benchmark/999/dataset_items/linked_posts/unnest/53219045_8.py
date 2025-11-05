def wen1(df):
    return df.set_index('A').B.apply(pd.Series).stack().reset_index(level=0).rename(columns={0: 'B'})

def wen2(df):
    return pd.DataFrame({'A':df.A.repeat(df.B.str.len()),'B':np.concatenate(df.B.values)})

def wen3(df):
    s = pd.DataFrame({'B': np.concatenate(df.B.values)}, index=df.index.repeat(df.B.str.len()))
    return s.join(df.drop('B', 1), how='left')

def wen4(df):
    return pd.DataFrame([[x] + [z] for x, y in df.values for z in y],columns=df.columns)

def chris1(df):
    vals = np.array(df.B.values.tolist())
    a = np.repeat(df.A, vals.shape[1])
    return pd.DataFrame(np.column_stack((a, vals.ravel())), columns=df.columns)

def chris2(df):
    vals = df.B.values.tolist()
    rs = [len(r) for r in vals]
    a = np.repeat(df.A.values, rs)
    return pd.DataFrame(np.column_stack((a, np.concatenate(vals))), columns=df.columns)
