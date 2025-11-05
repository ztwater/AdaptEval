import argparse

def mycall(self, parser, namespace, values, option_string=None):
    parser_name = values[0]
    arg_strings = values[1:]

    # set the parser name if requested
    if self.dest is not argparse.SUPPRESS:
        setattr(namespace, self.dest, parser_name)

    # select the parser
    try:
        parser = self._name_parser_map[parser_name]
    except KeyError:
        args = {'parser_name': parser_name,
                'choices': ', '.join(self._name_parser_map)}
        msg = _('unknown parser %(parser_name)r (choices: %(choices)s)') % args
        raise argparse.ArgumentError(self, msg)

    # CHANGES
    # parse all the remaining options into a new namespace
    # store any unrecognized options on the main namespace, so that the top
    # level parser can decide what to do with them
    newspace = argparse.Namespace()
    newspace, arg_strings = parser.parse_known_args(arg_strings, newspace)
    setattr(namespace, 'subspace', newspace) # is there a better 'dest'?

    if arg_strings:
        vars(namespace).setdefault(argparse._UNRECOGNIZED_ARGS_ATTR, [])
        getattr(namespace, argparse._UNRECOGNIZED_ARGS_ATTR).extend(arg_strings)

argparse._SubParsersAction.__call__ = mycall

# Main parser
main_parser = argparse.ArgumentParser()
main_parser.add_argument("--common")

# sub commands
subparsers = main_parser.add_subparsers(dest='command')

parser_a = subparsers.add_parser('command_a')
parser_a.add_argument("--foo")
parser_a.add_argument("--bar")

parser_b = subparsers.add_parser('command_b')
parser_b.add_argument("--biz")
parser_b.add_argument("--baz")

# parse
input = 'command_a --foo bar --bar val --filter extra'.split()
namespace = main_parser.parse_known_args(input)
print namespace

input = '--common test command_b --biz bar --baz val'.split()
namespace = main_parser.parse_args(input)
print namespace
