
from sys import getsizeof

v1 = sum([x ** 2 for x in range(1, 11)])             # list comprehension
print(f"v1 :{v1}")

v2 = sum((x ** 2 for x in range(1, 11)))             # Generator
print(f"v2 :{v2}")

print("-" * 60)

colec1 = [x ** 2 for x in range(10000)]
colec2 = (x ** 2 for x in range(10000))

print(f"Comprehension size of collection - 01 :{getsizeof(colec1)}")
print(f"Generator size of collection - 02     :{getsizeof(colec2)}")

