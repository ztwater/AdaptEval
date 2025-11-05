import sys

def my_function():
   return 'my_function() called'

sys.modules['pytest'].common_funct = my_function
