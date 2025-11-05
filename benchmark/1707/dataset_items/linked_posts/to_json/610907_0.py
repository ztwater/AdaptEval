try:
    getattr(someObject, 'someProperty')         
except AttributeError:
    print "Doesn't exist"
else
    print "Exists"
