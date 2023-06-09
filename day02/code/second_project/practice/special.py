class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("吃饭啦")

    def sport(self):
        print("开始运动！")

    def say(self, target):
        print("Hello", target)

    # 特殊方法
    def __str__(self):
        return f"姓名{self.name}，年龄{self.age}"


person = Person("张三", 12)
print(person.name, person.age)
person.eat()
person.sport()
person.say("珊珊")
# 重写str方法之后可以直接把对象的值打印出来
print(person)
