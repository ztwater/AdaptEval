x = tf.placeholder(tf.float32, [None, 20, 20, 10], name='input')
phase_train = tf.placeholder(tf.bool, name='phase_train')

# generate random noise to pass into batch norm
x_gen = tf.random_normal([50,20,20,10])
pt_false = tf.Variable(tf.constant(True))

#generate a constant variable to pass into batch norm
y = x_gen.eval()

[bn, bn_vars] = batch_norm(x, 10, phase_train)

tf.initialize_all_variables().run()
train_step = lambda: bn.eval({x:x_gen.eval(), phase_train:True})
test_step = lambda: bn.eval({x:y, phase_train:False})
test_step_c = lambda: bn.eval({x:y, phase_train:True})

# Verify that this is different as expected, two different x's have different norms
print(train_step()[0][0][0])
print(train_step()[0][0][0])

# Verify that this is same as expected, same x's (y) have same norm
print(train_step_c()[0][0][0])
print(train_step_c()[0][0][0])

# THIS IS DIFFERENT but should be they same, should only be reading from the ema.
print(test_step()[0][0][0])
print(test_step()[0][0][0])
