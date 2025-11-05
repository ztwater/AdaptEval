df.join(pd.DataFrame(df.B.tolist(),index=df.index).add_prefix('B_'))
Out[33]:
   A       B       C  B_0  B_1
0  1  [1, 2]  [1, 2]    1    2
1  2  [3, 4]  [3, 4]    3    4
