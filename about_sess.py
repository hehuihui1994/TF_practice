# -*- coding:utf-8 -*-


import tensorflow as tf

'''
two kinds of using session
'''

# create tensorflow structure start

matrix1 = tf.constant([[3,3]])
matrix2 = tf.constant([[2],
                        [2]])

product = tf.matmul(matrix1, matrix2)   # matrix multiply np.dot(matrix1, matrix2)

# create tensorflow structure end

##method 1
# sess = tf.Session()
# result = sess.run(product)
# print result
# sess.close()

##method 2
with tf.Session() as sess:
    result1 = sess.run(product)
    print result1