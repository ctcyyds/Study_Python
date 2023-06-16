"""
通过UDP扫描所有8000端口广播的数据
"""
import socket
import threading
import json
import time

from Practice.TCP_client import ChatClient
from utils import decode_data, clear_console

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
        keys = ["name", "ip", "port"]
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
                self.add_chatroom(recv_msg)
            except:
                pass

    def show_current_chatrooms(self):
        """
        展示刷新出来的聊天室列表
        :return: 当前聊天室列表
        """
        clear_console()
        print("当前聊天室列表：")
        print("=" * 50)
        room_list = list(self.chatrooms.values())  # 拿到聊天室信息
        # 将所有的values根据其name进行排序
        room_list.sort(key=lambda x: x["name"])
        # 拿到元素
        for index, value in enumerate(room_list):
            name = value["name"]
            ip = value["ip"]
            port = value["port"]
            # 按照格式打印聊天室信息
            print(f"{index}-->{name}({ip}:{port})")
        print("=" * 50)
        print("【Enter ->刷新列表】")
        print("【q   ->返回上一级】")
        print("=" * 50)
        return room_list

    def run(self):
        # 创建扫描子线程
        thread = threading.Thread(target=self.recv_broadcast_msg)
        thread.daemon = True
        thread.start()
        clear_console()
        # 等待三秒
        print("正在获取聊天室列表，请稍等3...")
        time.sleep(1)
        clear_console()
        print("正在获取聊天室列表，请稍等2..")
        time.sleep(1)
        clear_console()
        print("正在获取聊天室列表，请稍等1.")
        time.sleep(0.5)
        clear_console()

        while True:
            room_list = self.show_current_chatrooms()
            user_input = input("请输入你想要进入的聊天室：")
            if user_input == "q":  # 按下q是返回上一级
                print("已返回")
                break
            elif user_input == "":  # 按下【Enter】是刷新列表
                print("已刷新")
                continue
            elif user_input.isdigit():
                i = int(user_input)
                if 0 <= i < len(room_list):
                    chat_room = room_list[i]
                    return chat_room
                else:
                    print("---------Waring!!!---------")
                    print(f"Can't find 【{i}】chat room")
                    print("---------------------------")
                    time.sleep(2)


if __name__ == '__main__':
    scanner = UDP_Sacanner()
    room = scanner.run()
    print("进入", room)
    user_nickname = input("请输入您的昵称：")
    client = ChatClient(user_nickname)
    client.enter(room)

