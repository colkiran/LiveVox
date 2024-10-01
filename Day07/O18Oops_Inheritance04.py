
class Animal:

    def __init__(self):
        print("Animal Ctor....")
        self.a = 10

    def eat(self):
        print("Animals eat......")


    def fun(self):
        print("Animal class fun method")


class Person:

    def __init__(self):
        print("Person Ctor.....")
        self.p = 20

    def talk(self):
        print("Person talks")

    def fun(self):
        print("Person class fun method......")

class Girl(Person, Animal):

    def __init__(self):
        super().__init__()              # parent
        print("Girl Ctor.....")
        self.g = 30

    def walk(self):
        print("Girl walks......")



tina = Girl()
tina.eat()
tina.talk()
tina.walk()

print("-" * 60)
tina.fun()
print(tina.__dict__)


