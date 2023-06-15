import socket
import json
from utils import decode_data

# 定义服务器地址和端口号
SERVER_ADDRESS = ('192.168.23.44', 8001)

# 创建TCP套接字并连接到服务器
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(SERVER_ADDRESS)


# 循环发送消息和接收消息
def send_message():
    while True:
        # 发送消息
        message = input("Send a message: ")
        client_socket.send(message.encode())

        # 接收消息
        received_data = client_socket.recv(2048)
        data = decode_data(received_data)
        print(json.loads(data))


send_message()
client_socket.close()
