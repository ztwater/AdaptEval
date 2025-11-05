parse_roman('MMCMXCVIII')
     0 +=     1  <== cur, prev = 1, 0
     1 +=     1  <== cur, prev = 1, 1
     2 +=     1  <== cur, prev = 1, 1
     3 +=     5  <== cur, prev = 5, 1
     8 +=   100  <== cur, prev = 100, 5
   108 +=   -10  <== cur, prev = 10, 100
    98 +=  1000  <== cur, prev = 1000, 10
  1098 +=  -100  <== cur, prev = 100, 1000
   998 +=  1000  <== cur, prev = 1000, 100
  1998 +=  1000  <== cur, prev = 1000, 1000
2998
