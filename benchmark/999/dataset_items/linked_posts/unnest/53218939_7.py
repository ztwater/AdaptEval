s=pd.DataFrame([[x] + [z] for x, y in zip(df.index,df.B) for z in y])
s.merge(df,left_on=0,right_index=True)
Out[491]:
   0  1  A       B
0  0  1  1  [1, 2]
1  0  2  1  [1, 2]
2  1  1  2  [1, 2]
3  1  2  2  [1, 2]
