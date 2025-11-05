import types
def copy_func(f, name=None):
    return types.FunctionType(f.func_code, f.func_globals, name or f.func_name,
        f.func_defaults, f.func_closure)

def A():
    """A"""
    pass
B = copy_func(A, "B")
B.__doc__ = """B"""
