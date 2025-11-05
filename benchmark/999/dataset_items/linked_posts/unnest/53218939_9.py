df=pd.DataFrame({'A':[1,2],'B':[[1,2],[3,4]]})
from collections import ChainMap
d = dict(ChainMap(*map(dict.fromkeys, df['B'], df['A'])))
pd.DataFrame(list(d.items()),columns=df.columns[::-1])
Out[574]:
   B  A
0  1  1
1  2  1
2  3  2
3  4  2
