import os
import logging
import sys

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # FATAL
stderr = sys.stderr
sys.stderr = open(os.devnull, 'w')

import tensorflow as tf
tf.get_logger().setLevel(tf.compat.v1.logging.FATAL)
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
logging.getLogger('tensorflow').setLevel(tf.compat.v1.logging.FATAL)

sys.stderr = stderr

import absl.logging
logging.root.removeHandler(absl.logging._absl_handler)
absl.logging._warn_preinit_stderr = False
