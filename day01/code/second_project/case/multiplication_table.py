"""
用while循环打印九九乘法表
"""
# row = 1
# while row <= 9:
#     col = 1
#     while col <= row:
#         print("{}*{}={}".format(col, row, col * row), end="\t")
#         col += 1
#     print()
#     row += 1
"""
倒序的九九乘法表
"""
row = 9
while row >= 1:
    col = 1
    while col <= row:
        print("{}*{}={}".format(col, row, col * row), end="\t")
        col += 1
    print()
    row -= 1
