# close the TF2 logger
tf2logger = tf.get_logger()
tf2logger.error('Close TF2 logger handlers')
tf2logger.root.removeHandler(tf2logger.root.handlers[0])
