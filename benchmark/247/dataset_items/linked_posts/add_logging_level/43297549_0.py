def add_level(log_name,custom_log_module=None,log_num=None,
                log_call=None,
                   lower_than=None, higher_than=None, same_as=None,
              verbose=True):
    '''
    Function to dynamically add a new log level to a given custom logging module.
    <custom_log_module>: the logging module. If not provided, then a copy of
        <logging> module is used
    <log_name>: the logging level name
    <log_num>: the logging level num. If not provided, then function checks
        <lower_than>,<higher_than> and <same_as>, at the order mentioned.
        One of those three parameters must hold a string of an already existent
        logging level name.
    In case a level is overwritten and <verbose> is True, then a message in WARNING
        level of the custom logging module is established.
    '''
    if custom_log_module is None:
        import imp
        custom_log_module = imp.load_module('custom_log_module',
                                            *imp.find_module('logging'))
    log_name = log_name.upper()
    def cust_log(par, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if par.isEnabledFor(log_num):
            par._log(log_num, message, args, **kws)
    available_level_nums = [key for key in custom_log_module._levelNames
                            if isinstance(key,int)]

    available_levels = {key:custom_log_module._levelNames[key]
                             for key in custom_log_module._levelNames
                            if isinstance(key,str)}
    if log_num is None:
        try:
            if lower_than is not None:
                log_num = available_levels[lower_than]-1
            elif higher_than is not None:
                log_num = available_levels[higher_than]+1
            elif same_as is not None:
                log_num = available_levels[higher_than]
            else:
                raise Exception('Infomation about the '+
                                'log_num should be provided')
        except KeyError:
            raise Exception('Non existent logging level name')
    if log_num in available_level_nums and verbose:
        custom_log_module.warn('Changing ' +
                                  custom_log_module._levelNames[log_num] +
                                  ' to '+log_name)
    custom_log_module.addLevelName(log_num, log_name)

    if log_call is None:
        log_call = log_name.lower()

    setattr(custom_log_module.Logger, log_call, cust_log)
    return custom_log_module
