import tensorflow as tf
image = tf.random.normal(shape=(245, 245, 2))
tf.image.flip_up_down(image)
