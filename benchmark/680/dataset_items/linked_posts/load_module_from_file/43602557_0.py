from importlib.util import spec_from_loader, module_from_spec
from importlib.machinery import SourceFileLoader 

spec = spec_from_loader("module.name", SourceFileLoader("module.name", "/path/to/file.py"))
mod = module_from_spec(spec)
spec.loader.exec_module(mod)
