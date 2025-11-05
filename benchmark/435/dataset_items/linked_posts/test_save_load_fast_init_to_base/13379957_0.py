class B(object):
    x = 3

CopyOfB = type('CopyOfB', B.__bases__, dict(B.__dict__))

b = B()
cob = CopyOfB()

print b.x   # Prints '3'
print cob.x # Prints '3'

b.x = 2
cob.x = 4

print b.x   # Prints '2'
print cob.x # Prints '4'
