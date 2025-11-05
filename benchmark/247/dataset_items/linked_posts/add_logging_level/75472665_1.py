import logging

# add log-level DEBUGV

DEBUGV = 9  # slightly lower than DEBUG (10)
logging.addLevelName(DEBUGV, "DEBUGV")

class MyLogger(logging.Logger):
    """Inherit from standard Logger and add level DEBUGV."""

    def debugv(self, msg, *args, **kwargs):
        """Log 'msg % args' with severity 'DEBUGV'."""
        if self.isEnabledFor(DEBUGV):
            self._log(DEBUGV, msg, args, **kwargs)


logging.setLoggerClass(MyLogger)
