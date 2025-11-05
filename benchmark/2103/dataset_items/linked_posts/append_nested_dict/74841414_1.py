def m4(a,b):
    for k in a:
      a.get(k).update(b.get(k, {})) 
    return a
