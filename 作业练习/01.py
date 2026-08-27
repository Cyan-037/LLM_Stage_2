import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('128.0.0.1', 8888))

server.listen()

client, client_info = server.accept()

message = client.recv(1024)

print(f'客户端消息：{message.decode("utf-8")}')