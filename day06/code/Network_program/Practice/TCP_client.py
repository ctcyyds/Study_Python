import socket
import sys
import threading
import json
import time
from utils import decode_data, clear_console

BUFFER_SIZE = 4096


class ChatClient:
    def __init__(self, nickname):
        self.nickname = nickname
        self.chat_room = None
        self.msg_list = []
        # 创建TCP套接字
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 允许端口复用
        self.client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def recv_msg(self):
        # 创建连接
        server_addr = (self.chat_room['ip'], self.chat_room['port'])
        self.client_socket.connect(server_addr)

        # 把自己的昵称发送出去
        self.client_socket.send(self.nickname.encode())

        # 服务器把最近十条历史消息发送过来
        recv_data = self.client_socket.recv(BUFFER_SIZE)
        recv_msg = decode_data(recv_data)
        self.msg_list = json.loads(recv_msg)

        try:
            # 循环接收数据
            while True:
                data = self.client_socket.recv(BUFFER_SIZE)
                if data:
                    recv = decode_data(data)
                    self.msg_list.append(json.loads(recv))
                else:
                    break
        finally:
            if self.client_socket is not None:
                self.client_socket.close()
                self.client_socket = None

    def enter(self, room):
        self.chat_room = room
        threading.Thread(target=self.recv_msg, daemon=True).start()
        time.sleep(1.5)
        while True:
            clear_console()
            # 将之前的消息打印在控制台
            chat_room = self.chat_room['name']
            print(f"聊天室：【{chat_room}】共有消息：{len(self.msg_list)}条")
            print("-" * 50)
            # 将接收到的消息按照格式显示
            for msg in self.msg_list:
                """打印格式
                时间 昵称 IP&Port ：
                聊天文本
                """
                print(f"{msg['time']} {msg['nickname']} {msg['from']}")
                print(msg['message'])
                print()

            print("-" * 50)
            print("【Enter ->刷新列表】")
            print("【q   ->返回上一级】")
            print("=" * 50)
            user_input = input("请输入内容：\n")
            if user_input == "q":
                break
            elif user_input == "":
                continue
            else:
                self.client_socket.send(user_input.encode())
                time.sleep(0.5)


if __name__ == '__main__':
    try:
        room = {'name': 'test', 'ip': '192.168.137.1', 'port': 8001}
        client = ChatClient("刘看山")
        client.enter(room)
    except KeyboardInterrupt as e:
        print("->用户Ctrl+c退出")
        sys.exit(0)
