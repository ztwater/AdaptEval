from dotted.collection import DottedDict

assert DottedDict(dict(foo=dict(bar="baz")))["foo"]["bar"] == "baz"
assert DottedDict(dict(foo=dict(bar="baz")))["foo.bar"] == "baz"
assert DottedDict(dict(foo=dict(bar="baz"))).get("lorem.ipsum", None) is None
assert DottedDict(dict(foo=dict(bar="baz"))).get("lorem.ipsum", "default") == "default"
