
class Animal:

    def __init__(self):
        print("Animal Ctor.....")
        self.a = 10

    def eat(self):
        print("Animals eat.....")


class Bird(Animal):


    def fly(self):
        print("Birds fly.......")


class Fish(Animal):

    def swim(self):
        print("Fishes swim........")



cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()
print(cuckoo.__dict__)

print("-" * 60)

dolphin = Fish()
dolphin.eat()
dolphin.swim()
print(dolphin.__dict__)

print("-" * 60)
# any class that we create its a child class of object class

print(isinstance(cuckoo, Bird))
print(isinstance(cuckoo, Animal))
print(isinstance(cuckoo, object))
print(isinstance(cuckoo, Fish))
