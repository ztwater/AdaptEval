import sys


def query_yes_no(var_0, var_1="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
            It must be "yes" (the default), "no" or None (meaning
            an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    var_2 = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if var_1 is None:
        var_3 = " [y/n] "
    elif var_1 == "yes":
        var_3 = " [Y/n] "
    elif var_1 == "no":
        var_3 = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % var_1)

    while True:
        sys.stdout.write(var_0 + var_3)
        var_4 = input().lower()
        if var_1 is not None and var_4 == "":
            return var_2[var_1]
        elif var_4 in var_2:
            return var_2[var_4]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")
