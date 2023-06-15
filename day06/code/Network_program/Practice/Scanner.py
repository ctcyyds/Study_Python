"""
通过UDP扫描所有8000端口广播的数据
"""
import socket
import threading
import json
from utils import decode_data

BUFFER_SIZE = 2048


class UDP_Sacanner:
    def __init__(self):
        # 保存所有扫描到的房间
        # Key为发送端IP地址和端口，Value为发的消息内容
        self.chatrooms = {}

    def add_chatroom(self, recv_msg, ip_port):
        """
        必须是规定的格式
        :param recv_msg:广播数据
        :param ip_port: 广播发起地址
        :return:
        """
        try:
            chat_room = json.loads(recv_msg)
        except:
            return

        # 判断字典中是否包含规定的元素
        keys = ["name", "iP", "port"]
        for key in keys:
            if key not in chat_room:
                return
            if chat_room[key] == "":
                return
        ip, port = ip_port
        key = f"{ip}:{port}"
        self.chatrooms[key] = chat_room

    def recv_broadcast_msg(self):
        """
        在子线程中扫描所有8000的广播
        :return:
        """
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.bind(('', 8000))  # 绑定接收的端口
        # 接收数据
        while True:
            try:
                recv_data, ip_port = self.udp_socket.recvfrom(BUFFER_SIZE)
                recv_msg = decode_data(recv_data)
                self.dd_chatroom(recv_msg)
            except:
                pass

    def run(self):
        # 创建扫描子线程
        thread = threading.Thread(target=self.recv_broadcast_msg)
        thread.daemon = True
        thread.start()
        while True:
            user_input = input("请输入你想要进入的聊天室：")
            print(user_input)
            print(self.chatrooms)


if __name__ == '__main__':
    scanner = UDP_Sacanner()
    scanner.run()
