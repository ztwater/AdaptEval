>>> def foo():
...     x = 2
...     class Foo:
...         x = 5
...         y = [x for i in range(1)]
...     return Foo
... 
>>> dis.dis(foo.__code__.co_consts[2].co_consts[2])
  5           0 BUILD_LIST               0 
              3 LOAD_FAST                0 (.0) 
        >>    6 FOR_ITER                12 (to 21) 
              9 STORE_FAST               1 (i) 
             12 LOAD_DEREF               0 (x) 
             15 LIST_APPEND              2 
             18 JUMP_ABSOLUTE            6 
        >>   21 RETURN_VALUE         
