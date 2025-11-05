undefined = object()

class Widget:

    def __init__(self):
        self.bar = 1

    def zoom(self):
        print("zoom!")

a = Widget()

bar = getattr(a, "bar", undefined)
if bar is not undefined:
    print("bar:%s" % (bar))

foo = getattr(a, "foo", undefined)
if foo is not undefined:
    print("foo:%s" % (foo))

zoom = getattr(a, "zoom", undefined)
if zoom is not undefined:
    zoom()
