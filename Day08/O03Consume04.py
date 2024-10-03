import sys

from gurgaon.mymodule import greet, Employee

greet("Ajay Jadeja")

print("-" * 60)

emp1 = Employee("Kevin", 45000)
print(emp1)

print("-" * 60)
print("-" * 60)
from sys import path

for pth in path:
    print(pth)
