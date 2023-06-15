"""
TCP服务器
"""
# 1导入模块
import time
import socket
import threading
from utils import decode_data
import json

BUFFER_SIZE = 2048


def handle_client(tcp_client: socket.socket, client_addr: tuple):
    tcp_client.send("欢迎来到【雷阵雨】聊天室\r\n".encode())
    while True:
        client_data = tcp_client.recv(BUFFER_SIZE)

        # 捕获异常
        msg = decode_data(client_data)

        # 判断客户端是否有数据传输过来
        if client_data:
            # tcp_client.send("已收到\r\n".encode())
            tcp_client.send(f"【{client_addr}】:{msg}\r\n".encode())
            print(f"{client_addr}:{msg}")
        else:
            tcp_client.close()
            break


def udp_broadcast():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 设置允许发送广播
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)

    while True:
        # 发送广播
        message = {
            "Name": "雷阵雨聊天室",
            "IP": "192.168.23.44",
            "Port": "8001"
        }

        # 发送消息
        udp_socket.sendto(f"{json.dumps(message)}".encode('utf-8'), ('192.168.23.255', 8000))
        # udp_socket.sendto(f"{json.dumps(message)}\r\n".encode(''), ("192.168.23.255", 8000))

        time.sleep(2)


def server():
    # 2创建socket套接字
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 3绑定IP和端口号
    tcp_server.bind(('192.168.23.44', 8001))

    # 4使套接字设置为被动模式
    tcp_server.listen(128)
    print("===============服务器已启动================")

    # 5发送广播
    # udp_broadcast()
    thread1 = threading.Thread(target=udp_broadcast)
    thread1.daemon = True
    thread1.start()

    # 5等待客户端的连接
    while True:
        tcp_client, client_addr = tcp_server.accept()
        print(f"欢迎来自{client_addr}的用户进入")

        # 创建线程
        thread = threading.Thread(target=handle_client, args=(tcp_client, client_addr))

        # 设置为守护线程
        thread.daemon = True
        thread.start()


if __name__ == '__main__':
    server()
