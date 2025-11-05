class Foo(object):
    def __getattr__(self, attr):
        print "looking up", attr
        value = 42
        self.__dict__[attr] = value
        return value

f = Foo()
print f.x 
#output >>> looking up x 42

f.x = 3
print f.x 
#output >>> 3

print ('__getattr__ sets a default value if undefeined OR __getattr__ to define how to handle attributes that are not found')
