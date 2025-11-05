from argparse import ArgumentParser, Namespace


def parse_by_group(parser):
    """
    Create a nested namespace using the groups defined in the argument parser.
    Adapted from https://stackoverflow.com/a/56631542/6524027

    :param args: arguments
    :param parser: the parser
    :return:
    """
    assert isinstance(parser, ArgumentParser)
    args = parser.parse_args()

    # the first two groups are 'positional_arguments' and 'optional_arguments'
    pos_group, optional_group = parser._action_groups[
        0], parser._action_groups[1]
    args_dict = args._get_kwargs()
    pos_optional_arg_names = [arg.dest for arg in pos_group._group_actions] + [
        arg.dest for arg in optional_group._group_actions
    ]
    pos_optional_args = {
        name: value
        for name, value in args_dict if name in pos_optional_arg_names
    }
    other_group_args = dict()

    # If there are additional argument groups, add them as nested namespaces
    if len(parser._action_groups) > 2:
        for group in parser._action_groups[2:]:
            group_arg_names = [arg.dest for arg in group._group_actions]
            other_group_args[group.title] = Namespace(
                **{
                    name: value
                    for name, value in args_dict if name in group_arg_names
                })

    # combine the positiona/optional args and the group args
    combined_args = pos_optional_args
    combined_args.update(other_group_args)
    return Namespace(flat=args, **combined_args)
    # return Namespace(**combined_args)

