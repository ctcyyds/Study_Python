class Human:
    def eat(self):
        print("吃饭")


class Chinese(Human):
    def eat(self):
        print("我们使用筷子吃饭")


class American(Human):
    def eat(self):
        print("我们使用刀叉吃饭")


class Indian(Human):
    def eat(self):
        print("我们使用手吃饭")


# 不管是谁，只要有eat方法都可调用
def someone_eat(someone):
    someone.eat()


chinese = Chinese()
american = American()
indian = Indian()
chinese.eat()
american.eat()
indian.eat()
print("-" * 50)
someone_eat(chinese)
someone_eat(american)
someone_eat(indian)
