import os
import socket


def decode_data(data: bytes) -> str:
    try:
        msg = data.decode('utf-8')
    except UnicodeDecodeError as e:
        msg = data.decode('gbk')
    return msg


def clear_console():
    # 使用ANSI转义序列清空控制台内容
    os.system('cls' if os.name == 'nt' else 'clear')


def get_local_ip():
    """
    获取本机所有IP
    :return: IP列表
    """
    local_ips = ["127.0.0.1"]
    for ip in socket.gethostbyname_ex(socket.gethostname())[2]:
        local_ips.append(ip)

    local_ips.sort(reverse=True)
    return local_ips
