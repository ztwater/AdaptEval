class Hasher(dict):
    # https://stackoverflow.com/a/3405143/190597
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value

example_dict = Hasher()
print(example_dict['key1'])
# {}
print(example_dict['key1']['key2'])
# {}
print(type(example_dict['key1']['key2']))
# <class '__main__.Hasher'>
