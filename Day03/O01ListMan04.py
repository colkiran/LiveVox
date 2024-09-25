"""
sort   - sort will sort the original array
sorted - will take a copy of the list sort it  and return it
"""

print("sort".center(60,"-"))
l1= [6, 9, 5, 1, 10, 4, 8, 2, 3, 7]
print(f"l1 :{l1}")

res_asc = sorted(l1)
print(f"Ascending :{res_asc}")

res_desc = sorted(l1, reverse=True)
print(f"Descending :{res_desc}")

print("-" * 60)

l2 = [6,"zebra", 9, 'yellow', 5, 'blue', 1, 'white', 10, 'violet', 4, 'green', 8, 'pink',  2, 'maroon', 3, 'orange', 7, 'cat', 'dog', 'egg', 'apple', 198, 1654, 28, 2609, 271 ]

print(f"l2 :{l2}")
print()
print("-" * 60)
print()
res = sorted(l2, key=ascii)
print(f"res: {res}")

i = 0
for i in range(0, len(res)):
    if type(res[i]) == int:
        print(res[i], i)
        break

print("-" * 60)
print(f"res :{res[:i] + sorted(res[i:])}")

print("-" * 60)

cities = ['bangalore', 'chennai', 'thiruvananthapuram', 'delhi', 'kolkata'
          'vishakapatnam', 'ooty', 'mumbai']

print(f"cities :{cities}")
# sort it based on the no of characters

print("-" * 60)
res_asc = sorted(cities, key=len)
print(f"Ascending :{res_asc}")

res_desc = sorted(cities, key=len, reverse=True)
print(f"Descending :{res_desc}")

print("reversed".center(60, "-"))

l1= [6, 9, 5, 1, 10, 4, 8, 2, 3, 7]
print(f"l1 :{l1}")

res = list(reversed(l1))
print(f"res :{res}")
