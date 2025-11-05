import sys
import importlib.machinery

def load_module(name, filename):
    # If the Loader finds the module name in this list it will use
    # module_name.__file__ instead so we need to delete it here
    if name in sys.modules:
        del sys.modules[name]
    loader = importlib.machinery.ExtensionFileLoader(name, filename)
    module = loader.load_module()
    locals()[name] = module
    globals()[name] = module

load_module('something', r'C:\Path\To\something.pyd')
something.do_something()
