import importlib

dirname, basename = os.path.split(pyfilepath) # pyfilepath: '/my/path/mymodule.py'
sys.path.append(dirname) # only directories should be added to PYTHONPATH
module_name = os.path.splitext(basename)[0] # '/my/path/mymodule.py' --> 'mymodule'
module = importlib.import_module(module_name) # name space of defined module (otherwise we would literally look for "module_name")
