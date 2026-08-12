'''
可以接受任意数量客户端接入，每一次只服务1个客户端
和被服务的客户端沟通的时候，可以无限接收客户端发来的消息
知道客户端发来'bye'，服务器断开和这个客户端的连接
'''
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('0.0.0.0',8888))

server.listen()

while True:
    client, client_info = server.accept()

    # send_message = f'请问有什么可以帮你的？'
    # client.send(send_message.encode('utf-8'))
    # print(f'服务器：{send_message}')

    while True:
        try:
            recv_message = client.recv(1024)
            print(f'{client_info}:{recv_message.decode("utf-8")}')
            if recv_message.decode('utf-8') == 'bye':
                client.close()
                break
        except Exception as e:
            print('客户端消息不合规')

    client.close()
    print('服务器访问关闭')