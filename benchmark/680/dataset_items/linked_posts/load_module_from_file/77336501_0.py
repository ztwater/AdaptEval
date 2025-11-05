cls = `MyClass`
MyClass = getattr(__import__(cls, globals(), locals(), [cls], 0), cls)
