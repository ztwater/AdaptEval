def __arg_to_bool__(arg):
    """__arg_to_bool__

        Convert string / int arg to bool
    :param arg: argument to be converted
    :type arg: str or int
    :return: converted arg
    :rtype: bool
    """
    str_true_values = (
        '1',
        'ENABLED',
        'ON',
        'TRUE',
        'YES',
    )
    str_false_values = (
        '0',
        'DISABLED',
        'OFF',
        'FALSE',
        'NO',
    )

    if isinstance(arg, str):
        arg = arg.upper()
        if arg in str_true_values:
            return True
        elif arg in str_false_values:
            return False

    if isinstance(arg, int):
        if arg == 1:
            return True
        elif arg == 0:
            return False

    if isinstance(arg, bool):
        return arg

    # if any other value not covered above, consider argument as False
    # or you could just raise and error
    return False

[...]


args = ap.parse_args()
my_arg = options.my_arg
my_arg = __arg_to_bool__(my_arg)

