xs = [1,2,3,4,5,6,7,8]

def closure(method, param):
  def t(x):
    return method(x, param)
  return t

f = closure(pow, 2)
f(10)
f = closure(pow, 3)
f(10)
