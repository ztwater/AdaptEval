import types
def copy_func(f, name=None):
    return types.FunctionType(f.__code__, f.__globals__, name or f.__name__,
        f.__defaults__, f.__closure__)
def func1(x):
  return 2*x
func2=copy_func(func1)
print(func2(7))
