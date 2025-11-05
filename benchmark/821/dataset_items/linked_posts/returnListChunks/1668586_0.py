>>> def f(x, n, acc=[]): return f(x[n:], n, acc+[(x[:n])]) if x else acc
>>> f("Hallo Welt", 3)
['Hal', 'lo ', 'Wel', 't']
>>> 
