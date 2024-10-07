
from pickle import *

class Person:

    def __init__(self):
        self.name = "Sachin"
        self.age = 54

    def show(self):
        print("name :", self.name, "age :", self.age)


p1 = Person()
FW = open("ClsPickled.txt", "wb")
dump(p1, FW)
FW.close()

print("-" * 60)
print("unpickled data :")
FL = open("ClsPickled.txt", "rb")
p2 = load(FL)
p2.show()



