import inspect

def caller_name():
    frames = inspect.stack()
    caller_name = ''
    for f in frames:
        if f.function == '<module>':
            return caller_name
        caller_name = f.function

def a():
    caller = caller_name()
    print(f"'a' was called from '{caller}'")

def b():
    a()

def c():
    b()

c()
