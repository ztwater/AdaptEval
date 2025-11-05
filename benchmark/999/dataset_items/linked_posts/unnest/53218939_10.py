newvalues=np.dstack((np.repeat(df.A.values,list(map(len,df.B.values))),np.concatenate(df.B.values)))
pd.DataFrame(data=newvalues[0],columns=df.columns)
   A  B
0  1  1
1  1  2
2  2  1
3  2  2
