"""
求三位数的水仙花数
"""
arr = range(100, 1000)
for s in arr:
    baiwei = s // 100
    shiwei = s // 10 % 10
    gewei = s % 10
    if s == (baiwei ** 3 + shiwei ** 3 + gewei ** 3):
        print("水仙花数：{}={}+{}+{}".format(s, baiwei ** 3, shiwei ** 3, gewei ** 3))
# s += 1
