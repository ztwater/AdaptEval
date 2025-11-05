from re import compile, split    
dre = compile(r'(\d+)')
mylist.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in split(dre, l)])
