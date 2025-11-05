def logToRoot(message, *args, **kwargs):
    if logging.root.isEnabledFor(levelNum):
        logging.root._log(levelNum, message, args, **kwargs)
