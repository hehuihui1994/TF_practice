# -*- coding:utf-8 -*-

import numpy as np
import tensorflow as tf

'''y = 0.1x + 0.3  

print changes in parameter 

'''

# create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3


# create tensorflow structure start

Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y_p = Weights*x_data + biases

loss = tf.reduce_mean(tf.square(y_data - y_p))

optimizer = tf.train.GradientDescentOptimizer(0.1)

train = optimizer.minimize(loss)

init = tf.initialize_all_variables()

#create tensorflow structure end

sess = tf.Session()
sess.run(init)

for step in range(500):
    sess.run(train)
    if step%20 == 0:
        print('step:{} Weights:{} biases:{}'.format(step, sess.run(Weights),sess.run(biases)))