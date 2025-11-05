>>> spam = Spam.parse_obj({'foo': {'count': 4, 'size': None}, 'bars': [{'apple': 'x1', 'banana': 'y'}, {'apple': 'x2', 'banana': 'y2'}]})
>>> spam
Spam(foo=Foo(count=4, size=None), bars=[Bar(apple='x1', banana='y'), Bar(apple='x2', banana='y2')])
