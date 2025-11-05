import sys
parser = ...
if len(sys.argv)==1:
    parser.print_help()
    # parser.print_usage() # for just the usage line
    parser.exit()
args = parser.parse_args()
