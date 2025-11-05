df=pd.DataFrame({'A':[1,2],'B':[[1,2],[1,2]]})

out = pd.concat([df.loc[:,'A'],(df.B.apply(pd.Series))], axis=1, sort=False)

out = out.set_index('A').stack().droplevel(level=1).reset_index().rename(columns={0:"B"})

       A    B
   0    1   1
   1    1   2
   2    2   1
   3    2   2
