def f(dim,i): 
  d = dim-1 ; s = d
  while i<s: 
    s+=d ; d-=1
  return (dim-d, i-s+d)
