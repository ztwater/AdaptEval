import logging

TRACE = 5
logging.addLevelName(TRACE, 'TRACE')
FORMAT = '%(levelname)s:%(name)s:%(lineno)d:%(message)s'


logging.basicConfig(format=FORMAT)
l = logging.getLogger()
l.setLevel(TRACE)
l.log(TRACE, 'trace message')
l.setLevel(logging.DEBUG)
l.log(TRACE, 'disabled trace message')
