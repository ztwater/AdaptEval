df.set_index('A').B.apply(pd.Series).stack().reset_index(level=0).rename(columns={0:'B'})
Out[463]:
   A  B
0  1  1
1  1  2
0  2  1
1  2  2
