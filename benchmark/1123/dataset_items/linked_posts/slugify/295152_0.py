>>> s
'foo-bar#baz?qux@127/\\9]'
>>> "".join(x for x in s if x.isalnum())
'foobarbazqux1279'
