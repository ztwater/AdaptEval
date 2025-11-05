In [796]: df.iloc[select_indices].index
Out[796]: Index([u'b', u'd', u'e'], dtype='object')

In [797]: df.iloc[select_indices].index.tolist()
Out[797]: ['b', 'd', 'e']
