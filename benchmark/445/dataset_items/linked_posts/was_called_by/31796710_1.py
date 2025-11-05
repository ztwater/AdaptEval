@print_caller_name(4)
def foo():
    return 'foobar'

def bar():
    return foo()

def baz():
    return bar()

def fizz():
    return baz()

fizz()
