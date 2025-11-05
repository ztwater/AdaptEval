class FStr:
    def __init__(self, s):
        self._s = s
    def __repr__(self):
        return eval(f"f'{self._s}'")

...

template_a = FStr('The current name is {name}')

names = ["foo", "bar"]
for name in names:
    print (template_a)
