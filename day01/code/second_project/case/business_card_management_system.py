"""
名片管理系统
1.程序启动，显示名片管理系统欢迎界面，并显示功能菜单
2.用户根据数字选择不同的功能
    1新建名片（姓名，电话，QQ，邮件）
    2显示全部名片
    3,查询名片（查询到指定的名片用户可以选择修改或者删除名片）
    4退出系统
"""

# 定义列表保存所有的名片
all_card = []


def add():
    """
    增加新的名片
    元素：姓名、电话、QQ、邮箱
    :return: 无
    """
    print("功能：增加名片")
    name = input("请输入你的姓名：")
    phone = input("请输入你的电话：")
    qq = input("请输入你的QQ：")
    email = input("请输入你的邮箱：")
    card = [name, phone, qq, email]
    all_card.append(card)
    print("添加成功!")


def show():
    """
    展示所有的名片
    :return: 无
    """
    print("功能：展示所有名片")
    # 定义表头
    title = ["Name", "Phone", "QQ", "Email"]
    # 用空格把列表拼接成一个完整的字符串(使用enumerate可以获取列表的索引)
    for index, tit in enumerate(title):
        if index == 0:
            rst = tit.ljust(4, " ")
        elif index == 1:
            rst = tit.ljust(11, " ")
        elif index == 2:
            rst = tit.ljust(10, " ")
        else:
            rst = tit.ljust(10, " ")
        print(rst, end="\t")
    print()

    for card in all_card:
        print("\t".join(card))
    print("展示完成")


def ope_card(card):
    """
    对查询到的名片进行操作
    :return: 无
    """
    while True:
        print("1 删除该名片")
        print("2 修改该名片")
        print("3 退出查询服务")
        ser = int(input("请输入接下来办理的业务："))
        if ser == 1:
            all_card.remove(card)
            print("名片信息删除成功！")
        elif ser == 2:
            card[0] = input("请输入你的姓名：")
            card[1] = input("请输入你的电话：")
            card[2] = input("请输入你的QQ：")
            card[3] = input("请输入你的邮箱：")
            print("名片信息更新成功！")
        elif ser == 3:
            break
        else:
            print("输入指令错误，请输入正确的指令")


def find():
    """
    通过搜索名字的方法来查询名片
    :return:无
    """
    print("功能：查询名片")
    name = input("请输入要查询的名字")
    for card in all_card:
        # 判断名片夹里面有没有该名片
        if name == card[0]:
            # 进入相关操作
            ope_card(card)
            break
        else:
            print("查无此人，请重新查询")


while True:
    print("==========欢迎使用【名片管理系统V1.0】==========")
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print("4.退出系统")
    operation = int(input("请输入想要办理的业务："))
    if operation == 1:
        add()
    elif operation == 2:
        show()
    elif operation == 3:
        find()
    elif operation == 4:
        break
