names = ("鸣人", "佐助", "小樱")
# 元组的第二种写法
# names = "鸣人", "佐助", "小樱"
print(names, type(names))
# 元组不能修改

# 自动组包
s = "鸣人", "佐助", "小樱"
print(s, type(s))

# 自动解包
name1, name2, name3 = s
print(name1, name2, name3)
print("-" * 50)

# 元组的应用
a = 10
b = 20
# 交换a和b的值
b, a = (a, b)
print(a, b)
