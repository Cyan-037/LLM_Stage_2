'''
socket(套接字)进程之间通信的一个工具
目前只要跟网络相关的都跟socket有关
1. 建立连接使用`connect`函数
2. 关闭连接使用`close`函数
3. 发送数据使用`send`函数
4. 接收数据使用`recv`函数
'''

# 创建一个TCP协议下的socket对象
import socket

# encode 编码 -> 字符串转二进制
name = '周'
name_byte = name.encode('UTF-8')
print(name_byte, type(name_byte))

name_str = name_byte.decode('UTF-8')
print(name_str, type(name_str))

# 快捷方法的二进制转换，只适用于ASCII码范围，不包括中文
name_b = b'ithima3'
print(name_b, type(name_b))
