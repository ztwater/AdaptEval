def f_factory(i):
    def f():
        return i  # i is now a *local* variable of f_factory and can't ever change
    return f

for i in range(3):           
    f = f_factory(i)
    functions.append(f)
