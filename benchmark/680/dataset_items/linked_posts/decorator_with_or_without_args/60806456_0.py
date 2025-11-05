from functools import wraps

def memoize(fn=None, hours=48.0):
  def deco(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
      return fn(*args, **kwargs)
    return wrapper

  if callable(fn): return deco(fn)
  return deco
