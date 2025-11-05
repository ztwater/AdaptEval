def remove_argument(var_0, var_1):
    for action in var_0._actions:
        var_2 = action.option_strings
        if (var_2 and var_2[0] == var_1) or action.dest == var_1:
            var_0._remove_action(action)
            break

    for action in var_0._action_groups:
        for group_action in action._group_actions:
            var_2 = group_action.option_strings
            if (var_2 and var_2[0] == var_1) or group_action.dest == var_1:
                action._group_actions.remove(group_action)
                return
