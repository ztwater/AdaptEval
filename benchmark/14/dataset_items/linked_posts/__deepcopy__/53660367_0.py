class Base(object):
    def __init__(self):
        self.deep_cp_attr = None
        self.logger = logging.getLogger("logs")
        self.log_config = LoggerConfig(self.logger)

    def __deepcopy__(self, memodict={}):
        cpyobj = type(self)() # shallow copy of whole object 
        cpyobj.deep_cp_attr = copy.deepcopy(self.other_attr, memodict) # deepcopy required attr

        return cpyobj
