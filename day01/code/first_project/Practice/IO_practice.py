"""
用户输入整型变量a
用户输入整型变量b
计算输出a+b的值
"""
# a = int(input("请输入A的值："))
# b = int(input("请输入B的值："))
# sum = a + b
# print("a+b=", sum)

"""
收银员输入苹果的价格price，单位：元/斤
收银员输入客户购买苹果的重量weight。单位：斤
计算并输出需要付款的金额money
"""
# price = float(input("请输入商品的单价(元/斤)："))
# weight = float(input("请输入商品的重量(斤)："))
# money = price * weight
# print("需要支付", money, "元")

"""
打印名片
"""
company = input("请输入公司")
name = input("请输入姓名")
title = input("请输入职位")
phone = input("请输入电话")
email = input("请输入邮箱")
print("-" * 50)
print(company)
print()
print("%s (%s)" % (name, title))
print()
print("Tel:", phone)
print("Email:", email)
print("-" * 50)
