import sys
frame = sys._getframe().f_back
calling_method = frame.f_code.co_name
calling_class = frame.f_locals.get("self").__class__.__name__
