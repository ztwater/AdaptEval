x = OrderedSet([1, 2, -1, "bar"])
x.add(0)
assert list(x) == [1, 2, -1, "bar", 0]
