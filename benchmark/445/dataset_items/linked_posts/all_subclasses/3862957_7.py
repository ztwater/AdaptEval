import importlib
modname, _, clsname = name.rpartition('.')
mod = importlib.import_module(modname)
cls = getattr(mod, clsname)
