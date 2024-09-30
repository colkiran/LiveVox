
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.marks = {"Xth": '85%', "XIIth": '89%', 'Degree': '73%'}


    def __str__(self):
        return f"Name is {self.name}\nAge is {self.age}\nMarks is {self.marks}"



ply1 = Player("Sachin", 45)
# ply1.get_details()

print("-" * 60)

print(str(ply1))

print("-" * 60)

print(ply1)                 # implicitly call __str__
