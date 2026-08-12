'''
开发一个服务器，可以和无数的客户端通讯
每一次通讯只服务一个客户端，剩余的排队

'''

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
    # 128.0.0.1 表示自己电脑，但只能本机的程序连（单机），不允许别人从别的IP连入
    # 0.0.0.0 表示自己的电脑，也表示允许任何人从任何IP接入
    ('0.0.0.0', 8888)
)
print('服务器当前运行在8888端口')


# 3. 启动服务器，等待被客户端连接
# socket对象的listen()方法
server.listen()

# 4. 等待客户端接入,一次只服务一个，循环接入
while True:
    client, client_info = server.accept()
    print(f'客户端{client_info}已经接入')
    # 5. 给客户端发送消息
    client.send('你好呀客户端'.encode('utf-8'))

    # 6. 接收客户端的消息
    try:
        recv_data = client.recv(1024)
        print(f'收到客户端{client_info}的数据：{recv_data.decode("utf-8")}')
    except Exception as e:
        print(f'客户端{client_info}的数据不规范，无法显示')
    finally:
        # 7. 主动关闭连接
        client.close()
