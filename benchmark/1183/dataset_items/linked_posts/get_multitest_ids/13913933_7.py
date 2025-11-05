  2           0 LOAD_NAME                0 (__name__)
              3 STORE_NAME               1 (__module__)

  3           6 LOAD_CONST               0 (5)
              9 STORE_NAME               2 (x)

  4          12 BUILD_LIST               0
             15 LOAD_NAME                3 (range)
             18 LOAD_CONST               1 (1)
             21 CALL_FUNCTION            1
             24 GET_ITER            
        >>   25 FOR_ITER                12 (to 40)
             28 STORE_NAME               4 (i)
             31 LOAD_NAME                2 (x)
             34 LIST_APPEND              2
             37 JUMP_ABSOLUTE           25
        >>   40 STORE_NAME               5 (y)
             43 LOAD_LOCALS         
             44 RETURN_VALUE        
