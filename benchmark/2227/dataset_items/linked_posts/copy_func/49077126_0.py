import inspect

value = 3

def a():
    return inspect.stack()[1][0].f_globals['value']
