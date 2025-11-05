>>> foo.__code__.co_consts
(None, <code object Foo at 0x10a436030, file "<stdin>", line 2>, 'Foo')
>>> dis.dis(foo.__code__.co_consts[1])
  2           0 LOAD_FAST                0 (__locals__) 
              3 STORE_LOCALS         
              4 LOAD_NAME                0 (__name__) 
              7 STORE_NAME               1 (__module__) 
             10 LOAD_CONST               0 ('foo.<locals>.Foo') 
             13 STORE_NAME               2 (__qualname__) 

  3          16 LOAD_CONST               1 (5) 
             19 STORE_NAME               3 (x) 

  4          22 LOAD_CONST               2 (<code object <listcomp> at 0x10a385420, file "<stdin>", line 4>) 
             25 LOAD_CONST               3 ('foo.<locals>.Foo.<listcomp>') 
             28 MAKE_FUNCTION            0 
             31 LOAD_NAME                4 (range) 
             34 LOAD_CONST               4 (1) 
             37 CALL_FUNCTION            1 (1 positional, 0 keyword pair) 
             40 GET_ITER             
             41 CALL_FUNCTION            1 (1 positional, 0 keyword pair) 
             44 STORE_NAME               5 (y) 
             47 LOAD_CONST               5 (None) 
             50 RETURN_VALUE         
