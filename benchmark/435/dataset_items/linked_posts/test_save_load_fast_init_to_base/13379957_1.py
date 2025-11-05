class C(object):
    x = []

CopyOfC = type('CopyOfC', C.__bases__, dict(C.__dict__))

c = C()
coc = CopyOfC()

c.x.append(1)
coc.x.append(2)

print c.x   # Prints '[1, 2]' (!)
print coc.x # Prints '[1, 2]' (!)
