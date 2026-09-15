import numpy as np
'''
1. 创建2个二维a和b，内容不限，结构3*4
'''
a = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])

b = np.arange(1,13)
b = b.reshape((3,4))

print('a+b=',a + b)
print('a*b=',a*b)

c = np.ones((1,4))
print('c=',c)
print('a+c=',a+c)
print('b+c=',b+c)

print('a中的最大值：', np.max(a))
print('a中的最小值：', np.min(a))
print('b中最大值索引：', np.argmax(b))
print('b中最小值索引：', np.argmin(b))