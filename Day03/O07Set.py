
s1 = set()
print(f"s1 :{s1}")
print(type(s1))
print("-" * 60)

s2 = {1, 2, 3, 4, 5.1, 6.3, 7.9, 8.5, 10+5j, 11-7j, 'twelve', 'thirteen', 'fourteen', 'fifteen', True, False}
print(f"s2 :{s2}")
print("-" * 60)

s3 = set(range(1, 11))
print(f"s3 : {s3}")
print(type(s3))

print("-" * 60)
# add, update, pop, remove, discard

s1 = set()
print(f"s1 :{s1}")

s1.add(1)
s1.add(2)
s1.add(1)
s1.add(3)
s1.add(2)
s1.add(3)
s1.add(4)

print(f"s1 :{s1}")

s1.update([1, 2, 3])
s1.update([3, 4, 5])
s1.update([2, 3, 4])
s1.update([5, 6, 7])
s1.update([1, 2, 8])
s1.update([8, 7, 9])
s1.update([10, 5, 3])

print(f"s1 :{s1}")

res = s1.pop()
print(f"res :{res}")

res = s1.pop()
print(f"res :{res}")

print(f"s1 :{s1}")

s1.remove(8)

s1.remove(6)

# s1.remove(1)

print(f"s1 :{s1}")

s1.discard(4)
s1.discard(10)

s1.discard(1)
print(f"s1 :{s1}")

print("-" * 60)

A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(f"A :{A}")
print(f"B :{B}")

print("-" * 60)

print(f"A union B :{A | B}")
print(F"B union A :{B.union(A)}")

print("-" * 60)

print(f"A intersection B :{A & B}")
print(f"B intersection A :{B.intersection(A)}")

print("-" * 60)

print(f"A difference B :{A - B}")
print(f"B difference A :{B.difference(A)}")

print("-" * 60)

print(f"A symmetric difference B :{A ^ B}")
print(f"B symmetric difference A :{B.symmetric_difference(A)}")

print("-" * 60)
# frozensets - immutable

a = frozenset([1, 2, 3, 4, 5])
print(f"a :{a}")
print(type(a))

print("-" * 60)

l1 = [1, 2, 3]
l2 = [4, 5, 6]

print(F"l1 + l2 = {l1 + l2}")
# print(F"l1 - l2 = {l1 - l2}")

