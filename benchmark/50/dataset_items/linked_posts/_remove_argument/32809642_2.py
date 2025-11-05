In [24]: parser._actions
Out[24]: 
[_HelpAction(option_strings=['-h', '--help'], dest='help',....),
 _StoreAction(option_strings=['--arg2'], dest='arg2', nargs=None,...)]

In [25]: parser.print_help()
usage: ipython3 [-h] [--arg2 ARG2]

optional arguments:
  -h, --help   show this help message and exit
  --arg2 ARG2  A second one
