"""
判断输入的密码是否符合规范
"""
# 定义密码规范
container = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
while True:
    pwd = input("Please enter the password:")
    # 遍历输入的密码
    for i in pwd:
        # 判断输入的密码中有没有在我们定义的规范中
        if i not in container:
            print("密码不符合规范，请重新输入")
            print("密码只能包含字母、数字、下划线")
            break
    else:
        print("密码符合规范")
        break
