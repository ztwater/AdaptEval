for i in range(0,10):
    funcs.append((lambda i: lambda x: f(i, x))(i))
