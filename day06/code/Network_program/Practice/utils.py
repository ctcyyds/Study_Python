def decode_data(data: bytes) -> str:
    try:
        msg = data.decode('utf-8')
    except UnicodeDecodeError as e:
        msg = data.decode('gbk')
    return msg
