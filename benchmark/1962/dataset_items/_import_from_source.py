import inspect
import typing
from contextlib import contextmanager
# from importlib import util as import_module, reload
from importlib import import_module, reload

@contextmanager
def patch(object_, attribute_name, value):
    old_value = getattr(object_, attribute_name)
    try:
        setattr(object_, attribute_name, value)
        yield
    finally:
        setattr(object_, attribute_name, old_value)


def detect_type_checking_mode_modules_names(module_name):
    # https://stackoverflow.com/questions/54764937/detecting-modules-that-get-imported-on-condition
    # this method loads the module as default (Type checking false). Gets then module vars,
    # then turns on type checking and reloads the module to get the type checked vars.
    module = import_module(module_name)
    default_module_names = set(vars(module))
    with patch(typing, "TYPE_CHECKING", True):
        # reloading since ``importlib.import_module``
        # will return previously cached entry
        reload(module)
    type_checked_module_namespace = dict(vars(module))
    # resetting to "default" mode
    reload(module)

    return {
        name
        for name, content in type_checked_module_namespace.items()
        if name not in default_module_names and inspect.ismodule(content)
    }
