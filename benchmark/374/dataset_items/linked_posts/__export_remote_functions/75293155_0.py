def __export_remote_functions():

  def add(a, b):
    return a + b

  def prod(a, b):
    return a * b
  return (add, prod)

(add, prod) = __export_remote_functions()

executor.run_python_fn(add)(1, 2)
