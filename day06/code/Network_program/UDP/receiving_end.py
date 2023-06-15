"""
UDP接收端
"""
# 1导入模块
import socket

# 2创建字节套
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 3绑定端口号
udp_socket.bind(('', 8888))
while True:
    # 4接收数据（代码会阻塞在这里）
    data, addr = udp_socket.recvfrom(2048)

    # 捕获异常，使GBK或者UTF-8都可
    try:
        decode = data.decode('utf-8')
    except UnicodeDecodeError as e:
        decode = data.decode('gbk')

    if data:
        print(f"{addr}:{decode}")
        udp_socket.sendto("已收到".encode(), addr)
    else:
        print("已经断开连接")
        udp_socket.close()
        break
