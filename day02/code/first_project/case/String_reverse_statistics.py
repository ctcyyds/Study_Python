"""
设计一个程序，只能输入长度低于31的字符串
否则提示用户重新输入
"""
while True:
    s = input("请输入字符串")
    if len(s) >= 31:
        print("字符串超出规定，请重新输入！")
        continue

    # 打印输入的字符串
    print("你输入的字符串为：", s)
    # 打印字符串长度
    print("长度为：", len(s))
    # 打印逆序后的字符串
    ss = s[::-1]
    print("逆序后为：", ss)
    # 字符统计结果
    dic = dict()
    for i in s:
        # 一个字符的第一次统计
        if i not in dic:
            dic.setdefault(i, 1)
        # 一个字符的第二次统计
        else:
            dic[i] += 1
    rst = [f"{key}:{value}" for key, value in dic.items()]
    # 将列表组合成一个字符串
    join = " ".join(rst)
    print(join, type(join))
    break
