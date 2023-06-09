class Amimal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eat food")

    def sleep(self):
        print(f"{self.name} is slepping")


# 扩展能力
class Fly():
    def flying(self):
        print(f"{self.name} is flying")


# 会根据先继承谁就调用谁的方法
class Ducker(Amimal, Fly):
    def __init__(self, name):
        super().__init__(name)


ducker = Ducker("唐老鸭")
ducker.eat()
ducker.sleep()
ducker.flying()
