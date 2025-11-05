MY_LEVEL_NUM = 25
logging.addLevelName(MY_LEVEL_NUM, "MY_LEVEL_NAME")
def log_at_my_log_level(self, message, *args, **kws):
    # Yes, logger takes its '*args' as 'args'.
    self._log(MY_LEVEL_NUM, message, args, **kws)
logger.log_at_my_log_level = log_at_my_log_level
