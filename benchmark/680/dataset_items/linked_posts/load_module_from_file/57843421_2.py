import os, sys, inspect, copy

SOURCE_FILE = os.path.abspath(inspect.getsourcefile(lambda:0)).replace('\\','/')
SOURCE_DIR = os.path.dirname(SOURCE_FILE)

print("test::SOURCE_FILE: ", SOURCE_FILE)

# portable import to the global space
sys.path.append(TACKLELIB_ROOT) # TACKLELIB_ROOT - path to the library directory
import tacklelib as tkl

tkl.tkl_init(tkl)

# cleanup
del tkl # must be instead of `tkl = None`, otherwise the variable would be still persist
sys.path.pop()

tkl_import_module(SOURCE_DIR, 'testlib.py')

print(globals().keys())

testlib.base_test()
testlib.testlib_std1.std1_test()
testlib.testlib_std1.testlib_std2.std2_test()
#testlib.testlib.std3.std3_test()                             # does not reachable directly ...
getattr(globals()['testlib'], 'testlib.std3').std3_test()     # ... but reachable through the `globals` + `getattr`

tkl_import_module(SOURCE_DIR, 'testlib.py', '.')

print(globals().keys())

base_test()
testlib_std1.std1_test()
testlib_std1.testlib_std2.std2_test()
#testlib.std3.std3_test()                                     # does not reachable directly ...
globals()['testlib.std3'].std3_test()                         # ... but reachable through the `globals` + `getattr`
