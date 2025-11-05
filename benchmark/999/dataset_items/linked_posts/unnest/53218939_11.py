from itertools import cycle,chain
l=df.values.tolist()
l1=[list(zip([x[0]], cycle(x[1])) if len([x[0]]) > len(x[1]) else list(zip(cycle([x[0]]), x[1]))) for x in l]
pd.DataFrame(list(chain.from_iterable(l1)),columns=df.columns)
   A  B
0  1  1
1  1  2
2  2  1
3  2  2
