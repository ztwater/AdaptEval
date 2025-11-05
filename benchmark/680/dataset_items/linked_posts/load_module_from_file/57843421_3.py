# optional for 3.4.x and higher
#import os, inspect
#
#SOURCE_FILE = os.path.abspath(inspect.getsourcefile(lambda:0)).replace('\\','/')
#SOURCE_DIR = os.path.dirname(SOURCE_FILE)

print("1 testlib::SOURCE_FILE: ", SOURCE_FILE)

tkl_import_module(SOURCE_DIR + '/std1', 'testlib.std1.py', 'testlib_std1')

# SOURCE_DIR is restored here
print("2 testlib::SOURCE_FILE: ", SOURCE_FILE)

tkl_import_module(SOURCE_DIR + '/std3', 'testlib.std3.py')

print("3 testlib::SOURCE_FILE: ", SOURCE_FILE)

def base_test():
  print('base_test')
