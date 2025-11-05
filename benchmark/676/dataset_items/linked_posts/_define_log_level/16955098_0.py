import logging

SUBDEBUG = 5
logging.addLevelName(SUBDEBUG, 'SUBDEBUG')

def subdebug(self, message, *args, **kws):
    self.log(SUBDEBUG, message, *args, **kws) 
logging.Logger.subdebug = subdebug

logging.basicConfig()
l = logging.getLogger()
l.setLevel(SUBDEBUG)
l.subdebug('test')
l.setLevel(logging.DEBUG)
l.subdebug('test')
