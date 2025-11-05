from logging import getLoggerClass, addLevelName, setLoggerClass, NOTSET

VERBOSE = 5

class MyLogger(getLoggerClass()):
    def __init__(self, name, level=NOTSET):
        super().__init__(name, level)

        addLevelName(VERBOSE, "VERBOSE")

    def verbose(self, msg, *args, **kwargs):
        if self.isEnabledFor(VERBOSE):
            self._log(VERBOSE, msg, args, **kwargs)

setLoggerClass(MyLogger)
