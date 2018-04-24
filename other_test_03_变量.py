import tensorflow as tf

# 创建一个变量初始化为0
state = tf.Variable(0, name='count')

# 创建一个op， 作用是使state加1
new_value = tf.add(state, 1)

# 赋值ap
update = tf.assign(state, new_value)

# 变量的初始化
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(state))
    for i in range(5):
        sess.run(update)
        print(sess.run(state))


