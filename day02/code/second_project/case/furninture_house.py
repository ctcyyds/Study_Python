"""
家具分不同的类型，并占用不同的面积
输出家具信息的时候需要展示家具类型和占地面积
房子有自己的地址和占地面积
房子可以添加家具
    -房子的剩余面积可以容纳下添加家具的面积提示添加成功
    -反之添加失败
输出房子的信息需要展示房子地址、占地面积、剩余面积
查看房子中所有的家具信息
"""


# 创建房子类
class House:
    def __init__(self, address, area):
        self.area = area
        self.address = address
        # 记录房子剩下面积
        self.are = area
        # 用于保存家具信息
        self.furn = []

    # 增加家具方法
    def add_furn(self, furn):
        if self.are >= furn.area:
            self.furn.append(furn)
            # 添加一个家具后需要减少房子总面积
            self.are -= furn.area
            print(f"添加成功，房子剩余面积为：{self.are}")
        else:
            print("----------Waring----------")
            print(f"该家具面积为：{furn.area}")
            print(f"房子剩余面积{self.are}不够，不能添加！")
            print("--------------------------")

    # 重写str方法
    def __str__(self):
        return f"房子地址：{self.address} 房子总面积：{self.area} 剩余面积：{self.are}"


# 创建家具类
class Furn:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    # 重写str方法
    # def __str__(self):
    #     return f"家具名称：{self.name} 占地面积：{self.area}"

    def __repr__(self):
        return f"家具名称：{self.name} 占地面积：{self.area}"


# 创建对象
zhuozi = Furn("书桌", 12)
yizi = Furn("椅子", 10)
chuang = Furn("席梦思", 200)
print(zhuozi, yizi)
home = House("海景房", 200)
print(home)
# 添加桌子
home.add_furn(zhuozi)
print(home)
# 添加席梦思
home.add_furn(chuang)
print(home)
print(home.furn)
