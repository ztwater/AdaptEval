df=pd.DataFrame({'A':df.A.repeat(df.B.str.len()),'B':np.concatenate(df.B.values)})
df
Out[465]:
   A  B
0  1  1
0  1  2
1  2  1
1  2  2
