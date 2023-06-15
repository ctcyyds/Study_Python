"""
TCP客户端发送数据
"""
# 1导入socket模块
import socket

# 2创建套接字
"""
参数1
    AF_INET:IPV4协议
    AF_INET6:IPV6协议
参数2
    SOCK_STREAM:TCP协议
    sock.SOCK_DGRAM:UDP协议
"""
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3建立TCP连接（和服务端建立连接）(参数是一个元组，分别写着IP和端口号)
tcp_client.connect(('127.0.0.1', 8080))  # 这里的IP与端口都是服务器的配置

# 4发送数据（不能直接发字符串，要发字节数组）
tcp_client.send(b'hello')
tcp_client.send("猴赛雷".encode('utf-8'))

# 可以在发送完数据后接收服务端发送的数据
result = tcp_client.recv(2048)
print("收到回复：", result.decode('GBK'))

# 5关闭套接字
tcp_client.close()
