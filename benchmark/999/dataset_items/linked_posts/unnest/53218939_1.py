df = pd.DataFrame({'A': [1, 2, 3, 4],'B': [[1, 2], [1, 2], [], np.nan]})
df.B = df.B.fillna({i: [] for i in df.index})  # replace NaN with []
df.explode('B')

   A    B
0  1    1
0  1    2
1  2    1
1  2    2
2  3  NaN
3  4  NaN
