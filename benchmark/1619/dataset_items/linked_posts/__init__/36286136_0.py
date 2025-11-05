with graph.as_default():
    # [Variable and model creation goes here.]

    saver = tf.train.Saver()  # Gets all variables in `graph`.

with tf.Session(graph=graph) as sess:
    saver.restore(sess)
    # Do some work with the model....
