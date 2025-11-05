f=Foo()
json.dumps(f, cls=CustomJSONEncoder)

{"bar": "hello", "baz": "world", "modified": "2023-02-08T11:49:15.675837"}
