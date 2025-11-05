def _detect_ipython_zmq():
    """Detects if in an IPython environment using ZMQ (i.e. notebook/qtconsole/lab).

    Mostly derived from stackoverflow below:
    https://stackoverflow.com/questions/15411967/how-can-i-check-if-code-is-executed-in-the-ipython-notebook/24937408

    Returns:
        True if called in IPython notebook or qtconsole.
    """
    try:
        from IPython import get_ipython

        shell = get_ipython().__class__.__name__
        if shell == "ZMQInteractiveShell":
            return True  # Jupyter notebook or qtconsole
        elif shell == "TerminalInteractiveShell":
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:  # pragma: no cover
        return False  # Probably standard Python interpreter

