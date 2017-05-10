# -*- coding:utf-8 -*-


import tensorflow as tf

# construct tensorflow structure start 
state = tf.Variable(0, name = 'counter')
# print state.name
one = tf.constant(1)

new_value = tf.add(state, one)
update = tf.assign(state, new_value)

init = tf.initialize_all_variables()

# construct tensorflow structure end

with tf.Session() as sess:
    sess.run(init)
    for step in range(3):
        sess.run(update)
        print sess.run(state)