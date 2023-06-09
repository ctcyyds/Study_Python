class Dog:
    def eat(self):
        print("狗吃骨头")

    def say(self):
        print("小狗汪汪叫")


class Duck:
    def eat(self):
        print("鸭子吃虫子")

    def say(self):
        print("鸭子嘎嘎叫")


def some(some):
    some.eat()
    some.say()


dog = Dog()
duck = Duck()
some(dog)
some((duck))
