from __future__ import annotations
import copy
import functools
import types
from typing import TypeVar
T = TypeVar('T')

def copy_func(f: T, globals=None, module=None) -> T:
    """Based on:
        https://stackoverflow.com/a/6528148 (@Glenn Maynard)
        https://stackoverflow.com/a/13503277 (@unutbu)
        https://stackoverflow.com/a/49077211 (@Mad Physicist)
    """
    if globals is None:
        globals = copy.copy(f.__globals__)
    g = types.FunctionType(f.__code__, globals, name=f.__name__,
                           argdefs=f.__defaults__, closure=f.__closure__)
    g = functools.update_wrapper(g, f)
    if module is not None:
        g.__module__ = module
    g.__kwdefaults__ = copy.copy(f.__kwdefaults__)
    return g