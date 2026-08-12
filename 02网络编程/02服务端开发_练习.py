# 1.导包
import socket

# 2.创造类对象
server = socket.socket(
    socket.AF_INET,     # IPv4
    socket.SOCK_STREAM  # TCP协议
)

# 3.设定服务端IP和端口
server.bind(
    # (IP,端口)
    ('127.0.0.1', 8887)
)
print('服务器当前运行在8887端口')

# 4.进入接收模式
server.listen()

# 5.接收一个客户端
client, client_info = server.accept()
print(f'客户端{client_info}已经接入')

# 6.服务端给该客户端发送消息
client.send('欢迎来到这个服务器!'.encode('utf8'))

# 7.服务端接收该客户端的消息
rcv_info = client.recv(1024)
print(f'收到客户端消息：{rcv_info.decode("utf8")}')

# 8.服务端停止向该客户端服务
client.close()