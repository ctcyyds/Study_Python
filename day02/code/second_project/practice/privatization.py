"""
私有化
    -属性私有化
    -方法私有化
"""


class Person:
    def __init__(self, name):
        self.name = name
        self.__mimi = 3.1415926

    def __xiaopihao(self):
        print("haha")


person = Person("张三")
person.__mimi = 123
# 属性不可以强行调用，这里可以调用是因为上面新创建
print(person.__mimi)
# 方法不可以强行调用
print(person.__xiaopihao)
