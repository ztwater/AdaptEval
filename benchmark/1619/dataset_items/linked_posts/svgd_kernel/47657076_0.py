import tensorflow as tf
import tensorflow_probability as tfp
import numpy as np 

np.random.seed(0)   
x = np.random.normal(3.0, .1, 100)

median = tfp.stats.percentile(x, 50.0, interpolation='midpoint')

tf.Session().run(median)
