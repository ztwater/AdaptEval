class Foo(object): pass
class Bar(Foo): pass
class Baz(Foo): pass
class Bing(Bar): pass

# unutbu's approach
def all_subclasses(cls):
    return cls.__subclasses__() + [g for s in cls.__subclasses__()
                                       for g in all_subclasses(s)]

print(all_subclasses(vars()['Foo']))  # Fine because  Foo is in scope
# -> [<class '__main__.Bar'>, <class '__main__.Baz'>, <class '__main__.Bing'>]

def func():  # won't work because Foo class is not locally defined
    print(all_subclasses(vars()['Foo']))

try:
    func()  # not OK because Foo is not local to func()
except Exception as e:
    print('calling func() raised exception: {!r}'.format(e))
    # -> calling func() raised exception: KeyError('Foo',)

print(all_subclasses(eval('Foo')))  # OK
# -> [<class '__main__.Bar'>, <class '__main__.Baz'>, <class '__main__.Bing'>]

# using eval('xxx') instead of vars()['xxx']
def func2():
    print(all_subclasses(eval('Foo')))

func2()  # Works
# -> [<class '__main__.Bar'>, <class '__main__.Baz'>, <class '__main__.Bing'>]
