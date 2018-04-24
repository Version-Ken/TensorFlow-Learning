import tensorflow as tf

# fetch 就是可以同时运行多个op
input1 = tf.constant(3.0)
input2 = tf.constant(2.0)
input3 = tf.constant(5.0)
# 变量，就需要用到下面注释的init
# input4 = tf.Variable(4.0)

add = tf.add(input1, input4)
mul = tf.multiply(input2, add)


with tf.Session() as sess:
    # init = tf.global_variables_initializer()
    # sess.run(init)
    result = sess.run([mul, add])
    print(result)
