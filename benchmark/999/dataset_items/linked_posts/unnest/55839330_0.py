df=pd.DataFrame({'A':[1,2],'B':[[1,2],[1,2]]})

pd.concat([df['A'], pd.DataFrame(df['B'].values.tolist())], axis = 1)\
  .melt(id_vars = 'A', value_name = 'B')\
  .dropna()\
  .drop('variable', axis = 1)

    A   B
0   1   1
1   2   1
2   1   2
3   2   2
