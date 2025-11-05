>>> import dis
>>> def foo():
...     class Foo:
...         x = 5
...         y = [x for i in range(1)]
...     return Foo
... 
>>> dis.dis(foo)
  2           0 LOAD_BUILD_CLASS     
              1 LOAD_CONST               1 (<code object Foo at 0x10a436030, file "<stdin>", line 2>) 
              4 LOAD_CONST               2 ('Foo') 
              7 MAKE_FUNCTION            0 
             10 LOAD_CONST               2 ('Foo') 
             13 CALL_FUNCTION            2 (2 positional, 0 keyword pair) 
             16 STORE_FAST               0 (Foo) 

  5          19 LOAD_FAST                0 (Foo) 
             22 RETURN_VALUE         
