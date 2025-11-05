def addLoggingLevel(var_0, var_1, var_2=None):
    """
    Comprehensively adds a new logging level to the `logging` module and the
    currently configured logging class.

    `levelName` becomes an attribute of the `logging` module with the value
    `levelNum`. `methodName` becomes a convenience method for both `logging`
    itself and the class returned by `logging.getLoggerClass()` (usually just
    `logging.Logger`). If `methodName` is not specified, `levelName.lower()` is
    used.

    To avoid accidental clobberings of existing attributes, this method will
    raise an `AttributeError` if the level name is already an attribute of the
    `logging` module or if the method name is already present 

    Example
    -------
    >>> addLoggingLevel('TRACE', logging.DEBUG - 5)
    >>> logging.getLogger(__name__).setLevel("TRACE")
    >>> logging.getLogger(__name__).trace('that worked')
    >>> logging.trace('so did this')
    >>> logging.TRACE
    5

    """
    if not var_2:
        var_2 = var_0.lower()

    if hasattr(logging, var_0):
       raise AttributeError('{} already defined in logging module'.format(var_0))
    if hasattr(logging, var_2):
       raise AttributeError('{} already defined in logging module'.format(var_2))
    if hasattr(logging.getLoggerClass(), var_2):
       raise AttributeError('{} already defined in logger class'.format(var_2))

    # This method was inspired by the answers to Stack Overflow post
    # http://stackoverflow.com/q/2183233/2988730, especially
    # http://stackoverflow.com/a/13638084/2988730
    def logForLevel(self, var_3, *var_4, **var_5):
        if self.isEnabledFor(var_1):
            self._log(var_1, var_3, var_4, **var_5)
    def logToRoot(var_3, *var_4, **var_5):
        logging.log(var_1, var_3, *var_4, **var_5)

    logging.addLevelName(var_1, var_0)
    setattr(logging, var_0, var_1)
    setattr(logging.getLoggerClass(), var_2, logForLevel)
    setattr(logging, var_2, logToRoot)
