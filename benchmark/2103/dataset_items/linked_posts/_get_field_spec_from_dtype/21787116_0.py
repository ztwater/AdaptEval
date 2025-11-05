In [22]: a
Out[22]: 
array([(1., 2., 99), (3., 4., 75)], 
      dtype=[('x', '<f4'), ('y', '<f4'), ('code', '<i8')])

In [23]: a.dtype.fields
Out[23]: 
mappingproxy({'x': (dtype('float32'), 0),
              'y': (dtype('float32'), 4),
              'code': (dtype('int64'), 8)})

In [24]: for name, typ in a.dtype.fields.items():
   ....:     print("%-12s %-20s  %d" % (name, typ[0], typ[1]))
   ....:     
y            float32               0
x            float32               4
code         int64                 8
