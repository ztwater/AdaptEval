In [61]: p1=argparse.ArgumentParser(parents=[p],add_help=False)
In [62]: p1._actions
Out[62]: 
[_HelpAction(option_strings=['-h', '--help'], dest='help', nargs=0, const=None, default='==SUPPRESS==', type=None, choices=None, help='show this help message and exit', metavar=None),
 _StoreAction(option_strings=['--foo'], dest='foo', nargs=None, const=None, default=None, type=None, choices=None, help=None, metavar=None)]
