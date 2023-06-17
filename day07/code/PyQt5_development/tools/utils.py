import os


def decode_data(data: bytes) -> str:
    try:
        msg = data.decode('utf-8')
    except UnicodeDecodeError as e:
        msg = data.decode('gbk')
    return msg


def clear_console():
    # 使用ANSI转义序列清空控制台内容
    os.system('cls' if os.name == 'nt' else 'clear')
