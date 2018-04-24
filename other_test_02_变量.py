import tensorflow as tf

a = tf.Variable([6, 5])
b = tf.constant([3, 4])
# 增加一个减法op
sub = tf.subtract(a, b)
# 增加一个加法op
add = tf.add(a, b)

# 定义一个初始化变量的op
init = tf.global_variables_initializer()

with tf.Session() as sess:
    # 运行初始化
    sess.run(init)
    print(sess.run(sub))
    print(sess.run(add))



