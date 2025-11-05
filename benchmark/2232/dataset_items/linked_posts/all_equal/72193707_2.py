Python 3.10.4 on my Windows laptop:

iterable = ()
 914 ns   914 ns   916 ns  use_first_any
 917 ns   925 ns   925 ns  use_first_next
1074 ns  1075 ns  1075 ns  next_as_statement
1081 ns  1083 ns  1084 ns  original

iterable = (1,)
1290 ns  1290 ns  1291 ns  next_as_statement
1303 ns  1307 ns  1307 ns  use_first_next
1306 ns  1307 ns  1309 ns  use_first_any
1318 ns  1319 ns  1320 ns  original

iterable = (1, 2)
1463 ns  1464 ns  1467 ns  use_first_any
1463 ns  1463 ns  1467 ns  next_as_statement
1477 ns  1479 ns  1481 ns  use_first_next
1487 ns  1489 ns  1492 ns  original
