import imp

foo = imp.load_source('module.name', '/path/to/file.py')
foo.MyClass()
