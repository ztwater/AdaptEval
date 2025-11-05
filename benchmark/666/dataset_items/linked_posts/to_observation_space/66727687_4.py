>>> spam = Spam.parse_raw('{"foo": {"count": 4, "size": null}, "bars": [{"apple": "x1", "banana": "y"}, {"apple": "x2", "banana": "y"}]}')
>>> spam
Spam(foo=Foo(count=4, size=None), bars=[Bar(apple='x1', banana='y'), Bar(apple='x2', banana='y')])
