def all_subclasses(cls):
    return set(cls.__subclasses__()).union(
        [s for c in cls.__subclasses__() for s in all_subclasses(c)])

print(all_subclasses(Foo))
# {<class '__main__.Bar'>, <class '__main__.Baz'>, <class '__main__.Bing'>}
