# # 定义列表
# name_list = ["佐助", "鸣人", "小樱", "雏田", "志乃", "犬冢牙"]
# print(name_list[2])
# print(name_list[0])
# print("-" * 50)
#
# # 遍历列表
# for s in name_list:
#     print(s)
# print("-" * 50)
#
# # 增加列表元素
# name_list.append("日向宁次")
# print(name_list)
# print("-" * 50)
#
# # 删除列表元素
# # 通过value删除元素
# # name_list.remove("日向宁次")
# # 通过索引下标来删除元素
# name_list.pop(6)
# print(name_list)
# print("-" * 50)
#
# # 修改列表元素
# name_list[0] = "佐井"
# print(name_list)
#
# # 根据元素内容得到其索引
# index = name_list.index("鸣人")
# print(index)  # 这里需要注意的是，该索引不是字符串类型而是int类型

# 数组排序
# arr = [12, 5, 88, 32, 9, 21, 1]
# arr.sort()
# print(arr)
# # 数组倒序排列
# print("-" * 50)
# arr.sort(reverse=True)
# # arr.reverse()
# print(arr)

# list列表嵌套
# 与C的区别就是每一行不一定是固定的列数
students = [
    ["鸣人", "佐助", "小樱"],
    ["雏田", "志乃", "犬冢牙"]
]
print(students[0][2])
