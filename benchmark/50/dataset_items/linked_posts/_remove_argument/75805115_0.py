def disable_argument(parser: argparse.ArgumentParser, arg: str) -> None:
    """Disable an argument from a parser.

    Args:
        parser (argparse.ArgumentParser): Parser.
        arg (str): Argument to be removed.
    """
    def raise_disabled_error(action):
        """Raise an argument error."""
        def raise_disabled_error_wrapper(*args) -> str:
            """Raise an exception."""
            raise argparse.ArgumentError(action, f'Has been disabled!')
        return raise_disabled_error_wrapper

    for action in parser._actions:
        opts = action.option_strings
        if (opts and opts[0] == arg) or action.dest == arg:
            action.type = raise_disabled_error(action)
            action.help = argparse.SUPPRESS
            break
