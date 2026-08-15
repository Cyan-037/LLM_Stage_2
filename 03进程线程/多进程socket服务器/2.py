import socket

if __name__ == '__main__':
    client = socket.socket()

    client.connect(('192.168.137.1', 8888))

    while True:
        client_message = input('请输入对话: ')
        client.send(client_message.encode('utf-8'))
        print('发送成功')
        if client_message == 'bye':
            break

    client.close()