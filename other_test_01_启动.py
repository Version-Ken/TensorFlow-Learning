import tensorflow as tf
# 去除警告：Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 创建一个常量op
m1 = tf.constant([[3, 3]])

# 创建一个常量op
m2 = tf.constant([[2], [3]])

# 创建一个矩阵乘法op， 把m1和m2传入
product = tf.matmul(m1, m2)

# # 定义一个会话，启动默认图
# sess = tf.Session()
#
# # 调用sess的run方法执行矩阵乘法op
# # run(product)触发了图中三个op
# result = sess.run(product)
# print(result)
# sess.close()

# with 写法与上面效果是一样的，with结束后sess自动关闭，但是变量依旧存在
with tf.Session() as sess:
    # 调用sess的run方法执行矩阵乘法op
    # run(product)触发了图中三个op
    result = sess.run(product)
    print(result)



