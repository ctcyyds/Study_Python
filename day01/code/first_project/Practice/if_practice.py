"""
day = input("请输入节日：")
if day == "元旦":
    print("吃大餐")
elif day == "春节":
    print("吃饺子")
elif day == "端午节":
    print("吃粽子")
elif day == "中秋节":
    print("吃月饼")
else:
    print("发红包")
"""
import random

"""
火车站安检
有车票进行安检，并判断所带物品是否超重
没有车票拒绝按键
"""

"""
has_ticket = eval(input("是否有车票(0否，1是)"))
if has_ticket:
    weight = int(input("物品重量(Kg)"))
    if weight >= 20:
        print("请办理托运")
    else:
        print("一路顺风")
else:
    print("请购买车票再来")
"""

"""
与电脑进行手头剪刀布游戏
"""
while True:
    print("-" * 50)
    print("Game start!")
    print("Regulation:0=石头，1=剪刀，2=布")
    P1 = int(input("请输入你的手势："))
    com = random.randint(0, 3)
    if P1 == com:
        print("平局，决战到天亮！")
    elif (P1 == 0 and com == 1) or (P1 == 1 and com == 2) or (P1 == 2 and com == 0):
        print("P1 win P1 {}; com {};".format(P1, com))
    else:
        print("com win P1 {}; com {};".format(P1, com))
