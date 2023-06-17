import socket
from tools.utils import *
import threading

BUFFERSIZE = 2048


class TcpClient:

    def __init__(self, local_ip="", local_port=0):
        super().__init__()
        self.tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_client.bind((local_ip, local_port))

    def __connect_server(self, target_ip, target_port):
        print("连接{}：{}成功".format(target_ip, target_port))
        try:
            while True:
                recv_data = self.tcp_client.recv(BUFFERSIZE)
                if recv_data:
                    print(decode_data(recv_data))
                else:
                    break
        finally:
            self.tcp_client.close()

    def connect(self, target_ip, target_port):
        """
        连接到指定服务器,开启子线程，代码不会阻塞在这个方法里
        :param target_ip: 目标IP地址
        :param target_port: 目标端口号
        :return:
        """
        try:
            self.tcp_client.connect((target_ip, target_port))
            # 创建子线程
            thread = threading.Thread(target=self.__connect_server, args=(target_ip, target_port))
            thread.daemon = True
            thread.start()
        except Exception as e:
            print(f"连接{target_ip}：{target_port}失败", e)
            return False
        return True
