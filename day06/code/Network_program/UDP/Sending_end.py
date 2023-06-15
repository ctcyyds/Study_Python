"""
使用UDP协议发送数据
"""
# 1导入模块
import socket

# 2创建套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 3绑定IP&端口
udp_socket.bind(('', 8888))
# 4发送数据(参数1：要发送的内容  参数2：接收数据的对象)
data = "你好 陌生人".encode()
addr = ("127.0.0.1", 9999)
udp_socket.sendto(data, addr)
# 5关闭套接字
udp_socket.close()
