import logging

@property
def log(obj):
    logging.addLevelName(5, 'TRACE')
    myLogger = logging.getLogger(obj.__class__.__name__)
    setattr(myLogger, 'trace', lambda *args: myLogger.log(5, *args))
    return myLogger
