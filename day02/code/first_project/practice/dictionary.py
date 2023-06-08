"""
dict字典使用键值对来存储数据
key和value类型不限制
"""
d = {"中国": "China", "英国": "England", "美国": "America"}
# # 查询
# print(d["中国"])
#
# # 增加
# d["日本"] = "Japan"
# d.setdefault("法国", "France")
# print(d)
#
# # 删除
# del d["日本"]
# d.pop("法国")
# print(d)
#
# # 更新
# d["美国"] = "USA"
# print(d)

# 直接遍历
for key in d:
    print(key, d[key])

for value in d.values():
    print(value)

# 打包
for item in d.items():
    print(item, type(item))
# 解包
for k, v in d.items():
    print(k, v)
