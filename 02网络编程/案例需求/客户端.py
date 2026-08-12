'''
无限和服务器发送消息
发送到每一条消息都是input输入
当输入消息为bye的时候，结束连接
'''
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('192.168.137.1',8888))

while True:
    # try:
    #     recv_message = client.recv(1024)
    #     print(f'收到服务器消息：{recv_message.decode("utf-8")}')
    # except Exception as e:
    #     print('服务器输入不合规')

    send_message = input('请输入消息，bye退出: ')
    if send_message == 'bye':
        break
    client.send(send_message.encode('utf-8'))
    print('发送成功!')

client.close()