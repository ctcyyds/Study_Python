"""
TCP服务端
可接收和发送数据
"""
# 1.导入socket模块
import socket

# 2.创建套接字
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3.绑定IP和端口号(如果IP地址为空字符串表示所有网卡的端口都监听数据)
tcp_server.bind(('', 8888))
# 4.使套接字设置为被动模式(参数表示等待客户端链接的最大数)
# 此时套接字对象由主动连接模式变为被动连接模式
tcp_server.listen(128)
while True:
    # 5.等待客户端的连接（阻塞当前线程，有客户端连接进来释放阻塞）
    tcp_client, client_addr = tcp_server.accept()
    print(f"客户端：{client_addr}接入")
    while True:
        # 6.接收/发送数据
        client_data = tcp_client.recv(2048)
        if client_data:
            print(f"{client_addr}:{client_data.decode('gbk')}")
            # 发送数据表示已经收到
            tcp_client.send("已收到".encode())
        else:
            print(f"客户端{client_addr}断开连接")
            tcp_client.close()
            break
