"""
字符串练习
"""
# ss = "hello"
# # 获取字符串中的元素
# print(ss[2])
# # 遍历字符串
# for s in ss:
#     print(s)

"""
字符串判断
"""
# while True:
#     str = input("请输入字符串：")
#     print("isalpha字母：", str.isalpha())
#     print("isdecimal数字：", str.isdecimal())
#     # 判断是否h开头
#     print(str.startswith("h"))
#     # 判断是否0结束
#     print(str.endswith("o"))

"""
字符串查找与替换
"""
# 字符串查找索引
print("abcs".find("s"))
# 字符串从右边开始查找索引
print("absc".rfind("s"))

txt = "hello world!"
# 替换(前面为替换前的值，后面为替换后的值)
print(txt.replace("world", "life"))
