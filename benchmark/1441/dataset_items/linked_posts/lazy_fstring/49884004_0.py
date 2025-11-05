log = logging.getLogger(__name__)

def __deferred_flog(log, fstr, level, *args):
    if log.isEnabledFor(level):
        import inspect
        frame = inspect.currentframe().f_back.f_back
        try:
            fstr = 'f"""' + fstr + '"""'
            log.log(level, eval(fstr, frame.f_globals, frame.f_locals))
        finally:
            del frame
log.fdebug = lambda fstr, *args: __deferred_flog(log, fstr, logging.DEBUG, *args)
log.finfo = lambda fstr, *args: __deferred_flog(log, fstr, logging.INFO, *args)
