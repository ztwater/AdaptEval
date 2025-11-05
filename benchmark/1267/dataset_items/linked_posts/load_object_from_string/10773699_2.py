cls = "test.somemodule.Test"
module_name, class_name = cls.rsplit(".", 1)

somemodule = importlib.import_module(module_name)
