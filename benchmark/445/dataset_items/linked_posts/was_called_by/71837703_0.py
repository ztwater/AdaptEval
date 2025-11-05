import functools

# outside ur class
def printOuterFunctionName(func):
@functools.wraps(func)
def wrapper(self):
    print(f'Function Name is: {func.__name__}')
    func(self)    
return wrapper 

class A:
  @printOuterFunctionName
  def foo():
    pass
