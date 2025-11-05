>>> registered_classes = {}
>>> Base = declarative_base(cls=Base, class_registry=registered_classes)
>>> registered_classes.keys()
dict_keys(['Account', '_sa_module_registry', 'AccountType', ...])
