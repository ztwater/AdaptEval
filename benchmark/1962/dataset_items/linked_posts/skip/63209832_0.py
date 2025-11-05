import inspect

def skip_init_without_args(app, what, name, obj, would_skip, options):
    if name == '__init__':
        func = getattr(obj, '__init__')
        spec = inspect.getfullargspec(func)
        return not spec.args and not spec.varargs and not spec.varkw and not spec.kwonlyargs
    return would_skip

def setup(app):
    app.connect("autodoc-skip-member", skip_init_without_args)
