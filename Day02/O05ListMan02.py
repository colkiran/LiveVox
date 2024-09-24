
print("append".center(60, "-"))

l1 = list(range(1, 6))
print(f"l1 :{l1}")

l1.append(6)
l1.append(7)
l1.append(8)

print(f"l1 :{l1}")

l1.append([9, 10, 11, 12, 13])
print(f"l1 :{l1}")
# print 10, 11, 12

print(f"l1[8][1:4] :{l1[8][1:4]}")

print("extend".center(60, "-"))
l1 = list(range(2, 10, 2))
print(f"l1 :{l1}")

l1.extend([10, 12, 14, 16])
print(F"l1 :{l1}")

l1.extend([18])
print(f"l1 :{l1}")

print("insert".center(60, '-'))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.insert(1, 1.5)
l1.insert(3, 2.5)
l1.insert(5, 3.5)
l1.insert(7, 4.5)

print(f"l1 :{l1}")

l1.insert(15, 250)
print(f"l1 :{l1}")

print("pop".center(60, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

res = l1.pop(7)
print(f"res :{res}")

res = l1.pop(5)
print(f"res :{res}")

res = l1.pop()
print(f"res :{res}")

print(f"l1 :{l1}")

print("remove".center(60, "-"))
l1 = [1, 1, 1, 1, 2, 3, 1, 1, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2]
print(f"l1 :{l1}")

l1.remove(3)
print(f"l1 :{l1}")

l1.remove(3)
print(f"l1 :{l1}")

l1.remove(3)
print(f"l1 :{l1}")

print("clear".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.clear()
print(f"l1 :{l1}")
