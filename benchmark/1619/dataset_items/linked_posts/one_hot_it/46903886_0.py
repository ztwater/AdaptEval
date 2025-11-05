import tensorflow as tf
import numpy as np
import scipy.misc

img = scipy.misc.imread('aachen_000000_000019_gtFine_color.png', mode = 'RGB')
palette = np.array(
[[128,  64, 128],
 [244,  35, 232],
 [ 70,  70,  70],
 [102, 102, 156],
 [190, 153, 153],
 [153, 153, 153],
 [250, 170,  30],
 [220, 220,   0],
 [107, 142,  35],
 [152, 251, 152],
 [ 70, 130, 180],
 [220,  20,  60],
 [255,   0,   0],
 [  0,   0, 142],
 [  0,   0,  70],
 [  0,  60, 100],
 [  0,  80, 100],
 [  0,   0, 230],
 [119,  11,  32],
 [  0,   0,   0],
 [255, 255, 255]], np.uint8)

semantic_map = []
for colour in palette:
  class_map = tf.reduce_all(tf.equal(img, colour), axis=-1)
  semantic_map.append(class_map)
semantic_map = tf.stack(semantic_map, axis=-1)
# NOTE cast to tf.float32 because most neural networks operate in float32.
semantic_map = tf.cast(semantic_map, tf.float32)
magic_number = tf.reduce_sum(semantic_map)
print semantic_map.shape

palette = tf.constant(palette, dtype=tf.uint8)
class_indexes = tf.argmax(semantic_map, axis=-1)
# NOTE this operation flattens class_indexes
class_indexes = tf.reshape(class_indexes, [-1])
color_image = tf.gather(palette, class_indexes)
color_image = tf.reshape(color_image, [1024, 2048, 3])

sess = tf.Session()
# NOTE magic_number checks that there are only 1024*2048 1s in the entire
# 1024*2048*21 tensor.
magic_number_val = sess.run(magic_number)
assert magic_number_val == 1024*2048
color_image_val = sess.run(color_image)
scipy.misc.imsave('test.png', color_image_val)
