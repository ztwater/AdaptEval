import logging
from functools import partial, partialmethod


def add_logging_level(level_name, level_num, method_name=None):
    """
    Comprehensively adds a new logging level to the `logging` module and the
    currently configured logging class.

    `level_name` becomes an attribute of the `logging` module with the value
    `level_num`.
    `methodName` becomes a convenience method for both `logging` itself
    and the class returned by `logging.getLoggerClass()` (usually just
    `logging.Logger`).
    If `methodName` is not specified, `levelName.lower()` is used.

    To avoid accidental clobberings of existing attributes, this method will
    raise an `AttributeError` if the level name is already an attribute of the
    `logging` module or if the method name is already present

    Example
    -------
    >>> add_logging_level('TRACE', logging.DEBUG - 5)
    >>> logging.getLogger(__name__).setLevel('TRACE')
    >>> logging.getLogger(__name__).trace('that worked')
    >>> logging.trace('so did this')
    >>> logging.TRACE
    5

    """
    if not method_name:
        method_name = level_name.lower()

    if hasattr(logging, level_name):
        raise AttributeError(f'{level_name} already defined in logging module')
    if hasattr(logging, method_name):
        raise AttributeError(
            f'{method_name} already defined in logging module'
        )
    if hasattr(logging.getLoggerClass(), method_name):
        raise AttributeError(f'{method_name} already defined in logger class')

    # This method was inspired by the answers to Stack Overflow post
    # http://stackoverflow.com/q/2183233/2988730, especially
    # https://stackoverflow.com/a/35804945
    # https://stackoverflow.com/a/55276759
    logging.addLevelName(level_num, level_name)
    setattr(logging, level_name, level_num)
    setattr(
        logging.getLoggerClass(), method_name,
        partialmethod(logging.getLoggerClass().log, level_num)
    )
    setattr(logging, method_name, partial(logging.log, level_num))

