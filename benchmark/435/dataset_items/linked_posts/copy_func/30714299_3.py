def main():
    from logging import getLogger as _getLogger # pyflakes:ignore, must copy
    getLogger = copy_func(_getLogger)
    getLogger.__doc__ += '\n    This function is from the Std Lib logging module.\n    '
    assert getLogger.__doc__ is not _getLogger.__doc__
    assert getLogger.__doc__ != _getLogger.__doc__
