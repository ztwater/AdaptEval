from importlib.machinery import SourceFileLoader

foo = SourceFileLoader("module.name", "/path/to/file.py").load_module()
foo.MyClass()
