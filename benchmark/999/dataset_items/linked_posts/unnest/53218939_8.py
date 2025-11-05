df.reindex(df.index.repeat(df.B.str.len())).assign(B=np.concatenate(df.B.values))
Out[554]:
   A  B
0  1  1
0  1  2
1  2  1
1  2  2

#df.loc[df.index.repeat(df.B.str.len())].assign(B=np.concatenate(df.B.values))
