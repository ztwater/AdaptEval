@deprecated("use another function")
def some_old_function(x, y):
    return x + y


class SomeClass(object):
    @deprecated("use another method")
    def some_old_method(self, x, y):
        return x + y


@deprecated("use another class")
class SomeOldClass(object):
    pass


some_old_function(5, 3)
SomeClass().some_old_method(8, 9)
SomeOldClass()
