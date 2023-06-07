"""
关于三角形的练习
"""
"""
打印正三角形
"""
# row = 1
# while row <= 5:
#     print("*" * row)
#     row += 1
"""
打印倒三角形
"""
# row = 5
# while row >= 1:
#     print("*" * row)
#     row -= 1
"""
打印行数可变的正三角形
"""
row = int(input("Please enter the row count:"))
i = 1
while i <= row:
    print("*" * i)
    i += 1
