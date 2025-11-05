In[74]: df
Out[74]: 
    A   B             C             columnD
0  A1  B1  [C1.1, C1.2]                D1
1  A2  B2  [C2.1, C2.2]  [D2.1, D2.2, D2.3]
2  A3  B3            C3        [D3.1, D3.2]

In[75]: dfListExplode(df,['C','columnD'])
Out[75]: 
    A   B     C columnD
0  A1  B1  C1.1    D1
1  A1  B1  C1.2    D1
2  A2  B2  C2.1    D2.1
3  A2  B2  C2.1    D2.2
4  A2  B2  C2.1    D2.3
5  A2  B2  C2.2    D2.1
6  A2  B2  C2.2    D2.2
7  A2  B2  C2.2    D2.3
8  A3  B3    C3    D3.1
9  A3  B3    C3    D3.2
