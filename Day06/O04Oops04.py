
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player initailized......")

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

ply1 = Player("Sachin", 30)
ply1.get_details()

print("-" * 60)

ply2 = Player("Sourav", 29)
ply2.get_details()

print("-" * 60)
ply2.runs = 120
print("ply2 :\n", ply2.__dict__)

print("-" * 60)
print("ply1 :\n", ply1.__dict__)


