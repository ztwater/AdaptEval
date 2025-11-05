def redirect_output(fn=None,*,destination=None):
  destination = sys.stderr if destination is None else destination
  def wrapper(*args, **kwargs):
    ... # your code here
  if fn is None:
    def decorator(fn):
      return functools.update_wrapper(wrapper, fn)
    return decorator
  else:
    return functools.update_wrapper(wrapper, fn)
