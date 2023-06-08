# 获取长度
str = "hello"
print(len(str))

# 删除
lsr = [1, 2, 3, 4, 5, 6, 7]
# 根据索引删除
del lsr[2]
print(lsr)

# 比较
# 比较是对两个列表中每个元素逐个进行比较
a = [1, 2, 3]
b = [1, 2, 4]
print(a > b)
print(a < b)

# 字符串比较
# 实际上是按照ASCII上面的序号进行比较
stt = "hello"
stt1 = "hella"
print(a > b)

# 最大值和最小值获取
print(max(11, 22, 1))
print(min(1, 22, 0))

ls = [2, 1, 4, -5, 22, 55, 11, 0]
l1 = {2, 1, 4, -5, 22, 55, 11, 0}
l2 = (2, 1, 4, -5, 22, 55, 11, 0)
print(max(ls))
print(min(ls))
print(max(l1))
print(min(l2))
print(max(l1))
print(min(l2))
