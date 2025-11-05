import logging
logging.basicConfig(
    format='  %(levelname)-8.8s %(funcName)s: %(message)s',
)
logging.NOTE = 32  # positive yet important
logging.addLevelName(logging.NOTE, 'NOTE')      # new level
logging.addLevelName(logging.CRITICAL, 'FATAL') # rename existing

log = logging.getLogger(__name__)
log.note = lambda msg, *args: log._log(logging.NOTE, msg, args)
log.note('school\'s out for summer! %s', 'dude')
log.fatal('file not found.')
