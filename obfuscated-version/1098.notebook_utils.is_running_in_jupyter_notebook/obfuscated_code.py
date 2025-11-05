def is_notebook() -> bool:
    try:
        var_0 = get_ipython().__class__.__name__
        if var_0 == 'ZMQInteractiveShell':
            return True   # Jupyter notebook or qtconsole
        elif var_0 == 'TerminalInteractiveShell':
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False      # Probably standard Python interpreter
