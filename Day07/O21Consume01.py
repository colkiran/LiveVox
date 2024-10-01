
import mymodule as m
from mymodule import greet, Employee


print("Sports :", m.sports)
print("Runs :", m.runs)

print("-" * 60)

greet("Sachin")

print("-" * 60)

m.runs['t20'] = 5000
print(f"runs :{m.runs}")

print("-" * 60)

emp1 = Employee("Micheal", 34000)
print(emp1)

