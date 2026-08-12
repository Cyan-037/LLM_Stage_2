# 服务端，需要一个运行端口，
import socket  # 导包（python内置）

# 1. 创建socket对象（类对象）
server = socket.socket(
    socket.AF_INET,  # 本质是数字2，AF_INET IPv4地址(xxx.xxx.xxx.xxx)
    socket.SOCK_STREAM  # 本质是数字1，代表TCP协议
)

# 2. 选择IP地址和端口（IP地址就是自己电脑，端口随意，自定）
# socket对象的bind方法
server.bind(
    # (IP,端口)
    # 128.0.0.1 表示自己电脑
    # 在自己电脑的8888端口上运行，客户端通过8888端口接入服务器
    # 8888随意，自己定
    ('127.0.0.1', 8888)
)
print('服务器当前运行在8888端口')
# 3. 启动服务器，被客户端连接
# socket对象的listen()方法
server.listen()

# 4. 等待客户端接入
# socket对象的accept方法
# accept()方法返回一个元组，内含2个元素
# 元素1：客户端链接对象。此对象记录了客户端的一切特征，和客户端通讯使用这个对象
# 元素2：记录了客户端的IP和端口，可以自行取用
# accept()方法是阻塞式，如果客户端不接入，代码就卡在这
client, client_info = server.accept()
print(f'客户端{client_info}已经接入')

# 5. 给客户端发送消息
# 客户端连接对象的send方法
# 发送和接收都是二进制
# 服务器向客户端发消息
client.send('你好呀客户端'.encode('utf-8'))

# 6. 接收客户端的消息
# 客户端连接对象的recv方法
# 接收端也是二进制
# 1024，表示一次最多接受多少字节（byte），1024表示1024Byte == 1KB
recv_data = client.recv(1024)
print(f'收到客户端的数据：{recv_data.decode("utf-8")}')

# 7. 主动关闭连接
# close方法
client.close()