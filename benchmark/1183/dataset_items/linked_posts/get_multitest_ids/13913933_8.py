>>> foo.__code__.co_consts[1].co_consts
('foo.<locals>.Foo', 5, <code object <listcomp> at 0x10a385420, file "<stdin>", line 4>, 'foo.<locals>.Foo.<listcomp>', 1, None)
>>> dis.dis(foo.__code__.co_consts[1].co_consts[2])
  4           0 BUILD_LIST               0 
              3 LOAD_FAST                0 (.0) 
        >>    6 FOR_ITER                12 (to 21) 
              9 STORE_FAST               1 (i) 
             12 LOAD_GLOBAL              0 (x) 
             15 LIST_APPEND              2 
             18 JUMP_ABSOLUTE            6 
        >>   21 RETURN_VALUE         
