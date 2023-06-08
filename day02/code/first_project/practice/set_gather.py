# set集合是无序的，并且该集合的元素是唯一的
s = {"chen", "zhang", "liu", "wang"}
print(s)

# 查询
for ele in s:
    print(ele)

# 添加
s.add("li")
print(s)

# 移除（只能按照内容删除，不能按照索引）
s.remove("li")
s.discard("hahah")  # 如果移除不存在的成员不会报错
s.pop()  # 随机移除一个元素
#
