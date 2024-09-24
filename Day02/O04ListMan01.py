
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 60)
l2 = [1, 2, 3, 4, 5.1, 6.8, 7.2, 8.9, 10+2j, 11-3j, "twelve", 'thirteen', 'fourteen', 'fifteen', True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 60)
l3 = list(range(10, 101, 10))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 60)
# CRUD
l1 = list(range(1, 11))
print(f"l1 :{l1}")

# read
print(f"l1[2] :{l1[2]}")
print(f"l1[6] :{l1[6]}")
print(f"l1[-1] :{l1[-1]}")
print(f"l1[-9] :{l1[-9]}")

# iterating
for i in l1:
    print(i, end=" ")
print()

for i in range(0, len(l1)):
    print(l1[i], end=" ")
print()

print("-" * 60)
# updating - replace, add new element
print(f"l1 :{l1}")
# insertion
l1[5] = 500
l1[8] = 800

print(f"l1 :{l1}")

# del
del l1[7]
del l1[1]

print(f"l1 :{l1}")

print("-" * 60)
print(dir(l1))
