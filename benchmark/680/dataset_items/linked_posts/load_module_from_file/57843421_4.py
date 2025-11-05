# optional for 3.4.x and higher
#import os, inspect
#
#SOURCE_FILE = os.path.abspath(inspect.getsourcefile(lambda:0)).replace('\\','/')
#SOURCE_DIR = os.path.dirname(SOURCE_FILE)

print("testlib.std1::SOURCE_FILE: ", SOURCE_FILE)

tkl_import_module(SOURCE_DIR + '/../std2', 'testlib.std2.py', 'testlib_std2')

def std1_test():
  print('std1_test')
