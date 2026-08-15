'''
1. 每接入一个客户端，主进程就创建一个子进程负责和客户通讯
2. 每一个子进程和客户端都是无限收，直到客户端发来bye就close
'''
import multiprocessing as mp
import socket

def connect_client(client, client_info):
    name = mp.current_process().name
    print(f'子进程:{name}, 接入客户端{client_info}')
    while True:
        client_message = client.recv(1024).decode("utf-8")
        print(f'客户端{client_info}消息：{client_message}')
        if not client_message:
            print('用户切断连接')
            break
        if client_message == 'bye':
            print(f'子进程:{name}, 关闭客户端{client_info}连接')
            break

    client.close()

if __name__ == '__main__':
    # 创建服务器对象
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置ip和端口
    server.bind(('0.0.0.0',8888))

    # 接听
    server.listen()
    print('服务器已准备连接')

    # 无限接收(核心)
    while True:
        # 先接收
        client, client_info = server.accept()
        # 接收到了开始
        mp.Process(target=connect_client, args=(client, client_info)).start()