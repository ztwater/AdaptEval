cur, prev = (5, 1, 10), (5, 1, 10)
# Take one from cur and zip the rest
next(cur) + sum(... zip(cur, prev))
# 5 + ... zip( (1, 10), (5, 1, 10) )  ==>  5 + ... ((1, 5), (10, 1)) 
