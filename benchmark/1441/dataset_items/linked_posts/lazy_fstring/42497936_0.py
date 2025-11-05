>>> template_a = open('template.txt').read()
>>> names = 'foo', 'bar'
>>> for name in names:
...     print(eval(template_a))
...
The current name is foo
The current name is bar
