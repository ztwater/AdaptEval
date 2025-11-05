def unnesting(df, explode):
    idx = df.index.repeat(df[explode[0]].str.len())
    df1 = pd.concat([
        pd.DataFrame({x: np.concatenate(df[x].values)}) for x in explode], axis=1)
    df1.index = idx

    return df1.join(df.drop(explode, 1), how='left')


unnesting(df,['B','C'])
Out[609]:
   B  C  A
0  1  1  1
0  2  2  1
1  3  3  2
1  4  4  2
