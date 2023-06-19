import socket

from PyQt5.QtCore import pyqtSignal, QObject

from tools.utils import *
import threading

BUFFERSIZE = 2048


class TcpClient(QObject):
    msg_signal = pyqtSignal(str)

    def __init__(self, local_ip="", local_port=0):
        super().__init__()
        self.tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.tcp_client.bind((local_ip, local_port))

    def __connect_server(self, target_ip, target_port):
        print("连接{}：{}成功".format(target_ip, target_port))
        try:
            while True:
                recv_data = self.tcp_client.recv(BUFFERSIZE)
                if recv_data:
                    # print(decode_data(recv_data))
                    self.msg_signal.emit(decode_data(recv_data))
                else:
                    break
        except Exception as e:
            print("网络已断开！", e)
        finally:
            self.tcp_client.close()
            self.tcp_client = None

    def connect(self, target_ip, target_port):
        """
        连接到指定服务器,开启子线程，代码不会阻塞在这个方法里
        :param target_ip: 目标IP地址
        :param target_port: 目标端口号
        :return:
        """
        try:
            self.tcp_client.connect((target_ip, target_port))
            socket_name = self.tcp_client.getsockname()
            print("本机IP和端口：", socket_name)
            # 创建子线程
            thread = threading.Thread(target=self.__connect_server, args=(target_ip, target_port))
            thread.daemon = True
            thread.start()
            return True, socket_name
        except Exception as e:
            print(f"连接{target_ip}：{target_port}失败", e)
            return False, None

    def relase(self):
        self.tcp_client.close()

    def send(self, send_text):
        print("发送消息：", send_text)
        if self.tcp_client:
            self.tcp_client.send(send_text.encode('utf-8'))
