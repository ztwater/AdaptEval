def is_interactive():
    try:
        __IPYTHON__
        return True
    except NameError:
        return False
