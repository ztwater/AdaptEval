In [27]: foo1 = parser.add_argument('foo',help='foo 1 positional')
In [28]: foo2 = parser.add_argument('foo',help='foo 2 positional')
In [29]: parser.print_help()
usage: ipython3 [-h] [--arg2 ARG2] foo foo
positional arguments:
  foo          foo 1 positional
  foo          foo 2 positional
  ...
