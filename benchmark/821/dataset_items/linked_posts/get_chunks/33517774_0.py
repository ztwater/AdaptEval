Y = lambda f: (lambda x: x(x))(lambda y: f(lambda *args: y(y)(*args)))
chunks = Y(lambda f: lambda n: [n[0][:n[1]]] + f((n[0][n[1]:], n[1])) if len(n[0]) > 0 else [])
