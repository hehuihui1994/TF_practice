import tensorflow as tf

# construct tensorflow structure start

input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

result = tf.multiply(input1, input2)

# construct tensorflow structure start

with tf.Session() as sess:
    print sess.run(result, feed_dict = {input1:[2.], input2:[7.]})