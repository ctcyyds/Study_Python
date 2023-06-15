"""
字符串的编码和解码
"""
# 编码 encoding表示编码方式
bytes_arr = "猴赛雷".encode(encoding="utf-8")
print(bytes_arr, type(bytes_arr))
# 解码
string = bytes_arr.decode(encoding="utf-8")
print(string)
