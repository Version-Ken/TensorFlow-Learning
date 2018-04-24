import tensorflow as tf

# feed 就是数据先不定义好，在run的时候再传进去
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

output = tf.multiply(input1, input2)

with tf.Session() as sess:
    # feed 的数据类型以字典的形式传入
    print(sess.run(output, feed_dict={input1: [3.0], input2: [4.0]}))




