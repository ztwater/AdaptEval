''.join([z[0] for z in zip(*(list(s) for s in strings)) if all(x==z[0] for x in z)])
