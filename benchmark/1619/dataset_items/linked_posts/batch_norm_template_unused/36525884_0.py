from bn_class import *

with tf.name_scope('Batch_norm_conv1') as scope:
    ewma = tf.train.ExponentialMovingAverage(decay=0.99)                  
    bn_conv1 = ConvolutionalBatchNormalizer(num_filt_1, 0.001, ewma, True)           
    update_assignments = bn_conv1.get_assigner() 
    a_conv1 = bn_conv1.normalize(a_conv1, train=bn_train) 
    h_conv1 = tf.nn.relu(a_conv1)
