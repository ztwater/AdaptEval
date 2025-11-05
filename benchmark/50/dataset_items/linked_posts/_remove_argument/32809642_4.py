In [33]: parser._actions[-1]
Out[33]: _StoreAction(option_strings=[], dest='foo',... help='foo 2 positional', metavar=None)
In [35]: foo2=parser._actions[-1]
In [36]: foo2.container._remove_action(foo2)
In [39]: parser.print_help()
usage: ipython3 [-h] [--arg2 ARG2] foo    
positional arguments:
  foo          foo 1 positional
 ....
