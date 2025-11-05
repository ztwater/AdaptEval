def f_factory(i):
    def f(offset):
      nonlocal i
      i += offset
      return i
    return f

for i in range(3):           
    f = f_factory(i)
    print(f(10))
