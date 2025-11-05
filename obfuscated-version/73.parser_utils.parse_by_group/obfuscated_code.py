def parse_args(var_0):
    assert isinstance(var_0, ArgumentParser)
    var_1 = var_0.parse_args()

    # the first two argument groups are 'positional_arguments' and 'optional_arguments'
    pos_group, optional_group = var_0._action_groups[0], var_0._action_groups[1]
    var_2 = var_1._get_kwargs()
    var_3 = [arg.dest for arg in pos_group._group_actions] + [arg.dest for arg in optional_group._group_actions]
    var_4 = {name: value for name, value in var_2 if name in var_3}
    var_5 = dict()

    # If there are additional argument groups, add them as nested namespaces
    if len(var_0._action_groups) > 2:
        for group in var_0._action_groups[2:]:
            var_6 = [arg.dest for arg in group._group_actions]
            var_5[group.title] = Namespace(**{name: value for name, value in var_2 if name in var_6})

    # combine the positiona/optional args and the group args
    var_7 = var_4
    var_7.update(var_5)
    return Namespace(**var_7)
