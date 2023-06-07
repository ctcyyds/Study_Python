"""
函数的使用
"""

# # 声明函数
# def say_hello():
#     """
#     打印你好
#     :return:无返回值
#     """
#     print("Hello world")
#
#
# # 调用函数
# say_hello()

"""
函数的返回值
"""

# def max(a, b):
#     """
#     :param a:
#     :param b:
#     :return: a,b
#     """
#     if a > b:
#         return a
#     return b
#
#
# def run(a, b):
#     sum = a + b
#     sub = a - b
#     return sum, sub
#
#
# print("Max=", max(5, 7))
# sum, sub = run(5, 7)
# print(sum, sub)

"""
全局变量和局部变量
"""
# 定义全局变量
m = 10
n = 20


def func1():
    # 定义局部变量
    a = 123
    # 想要在函数里面更改全局变量的时候需要声明一下这就是全局变量
    global m
    m = 123
    print(f"func1 a={a} m={m}")


def func2():
    a = 321
    print("func2 a=", a)


func1()
func2()
