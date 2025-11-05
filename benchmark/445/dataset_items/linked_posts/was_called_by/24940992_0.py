import sys
print sys._getframe().f_back.f_code.co_name
