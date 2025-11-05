# easier to use version
def all_subclasses2(classname):
    direct_subclasses = eval(classname).__subclasses__()
    return direct_subclasses + [g for s in direct_subclasses
                                    for g in all_subclasses2(s.__name__)]

# pass 'xxx' instead of eval('xxx')
def func_ez():
    print(all_subclasses2('Foo'))  # simpler

func_ez()
# -> [<class '__main__.Bar'>, <class '__main__.Baz'>, <class '__main__.Bing'>]
