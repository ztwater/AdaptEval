# creating `def foo()` and its bytecode elided

Disassembly of <code object Foo at 0x104e97000, file "<stdin>", line 2>:
  2           0 RESUME                   0
              2 LOAD_NAME                0 (__name__)
              4 STORE_NAME               1 (__module__)
              6 LOAD_CONST               0 ('foo.<locals>.Foo')
              8 STORE_NAME               2 (__qualname__)

  3          10 LOAD_CONST               1 (5)
             12 STORE_NAME               3 (x)

  4          14 PUSH_NULL
             16 LOAD_NAME                4 (range)
             18 LOAD_CONST               2 (1)
             20 CALL                     1
             28 GET_ITER
             30 LOAD_FAST_AND_CLEAR      0 (.0)
             32 LOAD_FAST_AND_CLEAR      1 (i)
             34 LOAD_FAST_AND_CLEAR      2 (x)
             36 SWAP                     4
             38 BUILD_LIST               0
             40 SWAP                     2
        >>   42 FOR_ITER                 8 (to 62)
             46 STORE_FAST               1 (i)
             48 LOAD_GLOBAL              6 (x)
             58 LIST_APPEND              2
             60 JUMP_BACKWARD           10 (to 42)
        >>   62 END_FOR
             64 SWAP                     4
             66 STORE_FAST               2 (x)
             68 STORE_FAST               1 (i)
             70 STORE_FAST               0 (.0)
             72 STORE_NAME               5 (y)
             74 RETURN_CONST             3 (None)
