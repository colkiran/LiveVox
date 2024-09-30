
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Ctor.....")


    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    @classmethod
    def CreatePlayer(cls, fn, ln, age):
        print("Factory.....")
        return cls(f"{fn} {ln}", age)         # calls the constructor
             # Player("Rohit", 34)



ply1 = Player("Rohit", 34)
ply1.get_details()

print("-" * 60)
ply2 = Player.CreatePlayer("Virat", "Kholi", 35)
ply2.get_details()