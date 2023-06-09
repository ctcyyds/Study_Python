# 创建父类
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self, target):
        print(f"Hello from {self.name} to {target}")

    def play(self):
        print("Play game")


# 创建子类
class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score

    def go_school(self):
        print(f"{self.name}去考试，得了{self.score}分")


student = Student("张三", 16, 150)
student.go_school()
student.say("李四")
student.play()
