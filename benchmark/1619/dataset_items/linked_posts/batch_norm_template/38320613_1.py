test_error = sess.run(fetches=cross_entropy, feed_dict={x: batch_xtest, y_:batch_ytest, train_phase: False})
