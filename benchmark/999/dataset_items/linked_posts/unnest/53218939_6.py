pd.DataFrame([[x] + [z] for x, y in df.values for z in y],columns=df.columns)
Out[488]:
   A  B
0  1  1
1  1  2
2  2  1
3  2  2
