logtf = logging.getLogger('DST')
logtf.setLevel(logging.DEBUG)

# file handler
logfile='/tmp/tf_s.log'
fh = logging.FileHandler(logfile)
fh.setFormatter( logging.Formatter('fh %(asctime)s %(name)s %(filename)s:%(lineno)d :%(message)s') )
logtf.addHandler(fh)
logtf.info('writing to %s', logfile)
