import inspect
from IPython.core.magics.code import extract_symbols

obj = MyClass
cell_code = "".join(inspect.linecache.getlines(new_getfile(obj)))
class_code = extract_symbols(cell_code, obj.__name__)[0][0]
print(class_code)
