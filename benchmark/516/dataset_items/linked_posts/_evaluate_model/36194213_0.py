add_boolean_argument(parser, 'foo', default=True)
parser.parse_args([])                   # Whatever the default was
parser.parse_args(['--foo'])            # True
parser.parse_args(['--nofoo'])          # False
parser.parse_args(['--foo=true'])       # True
parser.parse_args(['--foo=false'])      # False
parser.parse_args(['--foo', '--nofoo']) # Error
