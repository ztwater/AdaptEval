import logging


TRACE = 5
"""more detail than debug"""

logging.basicConfig()
logging.addLevelName(TRACE,"TRACE")
logger = logging.getLogger('')
logger.debug("n")
logger.setLevel(logging.DEBUG)
logger.debug("y1")
logger.log(TRACE,"n")
logger.setLevel(TRACE)
logger.log(TRACE,"y2")
    
