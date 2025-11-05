def set_custom_logging_levels(config={}):
    """
        Assign custom levels for logging
            config: is a dict, like
            {
                'EVENT_NAME': EVENT_LEVEL_NUM,
            }
        EVENT_LEVEL_NUM can't be like already has logging module
        logging.DEBUG       = 10
        logging.INFO        = 20
        logging.WARNING     = 30
        logging.ERROR       = 40
        logging.CRITICAL    = 50
    """
    assert isinstance(config, dict), "Configuration must be a dict"

    def get_level_func(level_name, level_num):
        def _blank(self, message, *args, **kws):
            if self.isEnabledFor(level_num):
                # Yes, logger takes its '*args' as 'args'.
                self._log(level_num, message, args, **kws) 
        _blank.__name__ = level_name.lower()
        return _blank

    for level_name, level_num in config.items():
        logging.addLevelName(level_num, level_name.upper())
        setattr(logging.Logger, level_name.lower(), get_level_func(level_name, level_num))

