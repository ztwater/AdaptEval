import pkgutil
import importlib

packages = pkgutil.walk_packages(path='.')
for importer, name, is_package in packages:
    mod = importlib.import_module(name)
    # do whatever you want with module now, it's been imported!
