
values = list(range(10, 31, 10))
print(f"values :{values}")

# upack
a, b, c = values
print(a, b, c, sep = ", ")

print("-" * 60)
values = list(range(10, 101, 10))
print(f"values :{values}")

a, b, *c = values
print(a, b, c, sep = ", ")

print("-" * 60)
a, *b, c = values
print(a, b, c, sep = ", ")

print("-" * 60)
*a, b, c = values
print(a, b, c, sep = ", ")

print("-" * 60)
lst1 = [1, 2, 3, 4, 5]
lst2 = [11, 22, 33, 44, 55]

lst3 = [lst1, lst2]
print(f"lst3 :{lst3}")
print(len(lst3))

print("-" * 60)
lst4 = [lst1 + lst2]
print(f"lst4 :{lst4}")
print(len(lst4))

print("-" * 60)
lst5 = [*lst1, *lst2]
print(f"lst5 :{lst5}")
print(len(lst5))

print("-" * 60)
letters = ['a', 'b', 'c', 'd', 'e', 'f']
print(f"letters :{letters}")

for letter in letters:
    print(letter, end=" ")
print()

print("-" * 60)
for letter in enumerate(letters):
    print(letter, end=" ")
print()

print("-" * 60)
for letter in enumerate(letters):
    print(letter[0], "\t", letter[1])

print("-" * 60)
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(my_list)

print("-" * 60)
for list in my_list:
    print(list)

print("-" * 60)
for list in enumerate(my_list):
    print(list[0], end="")
    print()
    for j in enumerate(list[1]):
        print("\t",j[0], "\t",  j[1])

print("-" * 60)
