# Main parser
main_parser = argparse.ArgumentParser()
main_parser.add_argument("-common")

filter_parser = argparse.ArgumentParser(add_help=False)
filter_parser.add_argument("--filter1", action=GroupedAction, dest='filter.filter1', default=argparse.SUPPRESS)
filter_parser.add_argument("--filter2", action=GroupedAction, dest='filter.filter2', default=argparse.SUPPRESS)

subparsers = main_parser.add_subparsers(help='sub-command help')

parser_a = subparsers.add_parser('command_a', help="command_a help", parents=[filter_parser])
parser_a.add_argument("--foo")
parser_a.add_argument("--bar")
parser_a.add_argument("--bazers", action=GroupedAction, dest='anotherGroup.bazers', default=argparse.SUPPRESS)
...
namespace = main_parser.parse_args()
print namespace
