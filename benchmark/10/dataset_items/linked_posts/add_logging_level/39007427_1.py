logging.setLoggerClass(MyLogger)
log = logging.getLogger(__name__)
# ...
log.trace("something specific")
