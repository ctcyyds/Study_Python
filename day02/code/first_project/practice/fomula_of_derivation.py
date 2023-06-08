"""
轻量级循环创建数据的方式
对列表或可迭代对象中的每个元素应用某种操作
用生成的结果创建新的列表
或者用满足特定条件的元素创建子序列
"""

# 列表推导式
# 通过for循环遍历所有元素，符合后边if判断，根据前面公式保留结果
lst = [i for i in range(0, 7) if i % 2 == 0]
print(lst)

# 元组推导式
t = (i for i in range(0, 7) if i % 2 == 0)
print(list(t))

# 集合推导式
s = {i for i in range(0, 7) if i % 2 == 0}
print(s)

# 字典推导式
# 把两个列表组合成一个，每个元素包括两个一一对应的元素
rst = zip(range(1, 10), range(21, 30))
print(list(rst))
# zip类型数据需要重复读取的话需要提前做转换
d = {key: value for key, value in zip(range(1, 10), range(21, 30))}
print(d)
