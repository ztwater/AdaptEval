def redirected_output(*fn,**options):
  destination = options.pop('destination', sys.stderr)
  if options:
    raise TypeError("unsupported keyword arguments: %s" % 
                    ",".join(options.keys()))
  def wrapper(*args, **kwargs):
    ... # your code here
  if fn:
    return functools.update_wrapper(wrapper, fn[0])
  else:
    def decorator(fn):
      return functools.update_wrapper(wrapper, fn)
    return decorator
