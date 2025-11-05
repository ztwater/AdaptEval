import importlib

cls = "somemodule.Test"
module_name, class_name = cls.split(".")

somemodule = importlib.import_module(module_name)

print(getattr(somemodule, class_name))
