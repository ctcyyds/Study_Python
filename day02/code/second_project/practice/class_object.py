"""
类和对象的基本知识
"""


# 定义一个类
class Person:
    # 初始化方法,可以在这里设定参数,这样的话不会把数据写死
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("我们要吃饭")

    def sport(self):
        # 内部调用方法的时候可以直接用self直接调用
        self.say("Let's go!")
        print("我们要运动")

    def say(self, target):
        print("你好", target)


# 创建一个对象
person = Person("张珊", 12)
# 调用类里面的属性和方法
print(person.name, person.age)
person.eat()
person.sport()
person.say("李华")
