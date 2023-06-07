"""
有六个人随机分配班级
"""
import random

# 确定人员
names = ["鸣人", "佐助", "小樱", "雏田", "志乃", "犬冢牙"]
# 确定有几个班级
cla = [
    [],
    [],
    []
]

for name in names:
    # 随机指定一个班级
    index = random.randint(0, 2)
    # 往班级列表增加人员
    cla[index].append(name)
print("分配结果:", cla)
