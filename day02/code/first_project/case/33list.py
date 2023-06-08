"""
分组一个list里面的元素
[1,2,3,...,100]==>[[1,2,3],[4,5,6],...,[100]]
"""
lst = list(range(1, 101))
print(lst)
arr = [lst[i:i + 3] for i in range(len(lst)) if i % 3 == 0]
print(arr)
