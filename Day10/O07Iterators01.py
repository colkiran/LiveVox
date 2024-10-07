
l = ['a', 'b', 'c', 'd', 'e']
print(f"list :{l}")

# print(dir(l))

iterObject = l.__iter__()
# print(dir(iterObject))

# __next__ and __iter__ are the protocols of iterable objects

elem1 = iterObject.__next__()
print(f"elem1 :{elem1}")
elem2 = iterObject.__next__()
print(f"elem2 :{elem2}")
elem3 = iterObject.__next__()
print(f"elem3 :{elem3}")
elem4 = iterObject.__next__()
print(f"elem4 :{elem4}")
elem5 = iterObject.__next__()
print(f"elem5 :{elem5}")

# StopIteration
# elem6 = iterObject.__next__()
# print(f"elem6 :{elem6}")

print("-" * 60)
for x in l:
    print(x)
