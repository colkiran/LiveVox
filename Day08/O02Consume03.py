
import sys

# print(sys.path)             # list
sys.path.append("C:\\Delhi")

for pth in sys.path:
    print(pth)

from gurgaon.mymodule import greet, Employee

print("-" * 60)

greet("Kapil Dev")

print("-" * 60)

emp1 = Employee("David", 12500)
print(emp1)
