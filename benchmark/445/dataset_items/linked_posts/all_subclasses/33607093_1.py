@classmethod
def get_subclasses(cls):
    for subclass in cls.__subclasses__():
        yield from subclass.get_subclasses()
        yield subclass
