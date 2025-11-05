import deprecation

@deprecation.deprecated(details="Use bar instead")
def foo():
    print("Foo")


def bar():
    print("Bar")


foo()

bar()
