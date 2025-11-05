s=pd.DataFrame({'B':np.concatenate(df.B.values)},index=df.index.repeat(df.B.str.len()))
s.join(df.drop('B',1),how='left')
Out[477]:
   B  A
0  1  1
0  2  1
1  1  2
1  2  2
