import importlib
import importlib.machinery
import importlib.util

pkg = "mypkg"
spec = importlib.machinery.PathFinder().find_spec(pkg, ["/path/to/mypkg-parent"])
mod = importlib.util.module_from_spec(spec)
sys.modules[pkg] = mod  # needed for exec_module to work
spec.loader.exec_module(mod)
sys.modules[pkg] = importlib.import_module(pkg)
