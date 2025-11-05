df = pd.DataFrame({'BoolCol': [True, False, False, True, True]},
       index=[10,20,30,40,50])

In [53]: df
Out[53]: 
   BoolCol
10    True
20   False
30   False
40    True
50    True

[5 rows x 1 columns]

In [54]: df.index[df['BoolCol']].tolist()
Out[54]: [10, 40, 50]
