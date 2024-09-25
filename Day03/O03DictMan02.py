
print("keys".center(60, '-'))

player = {'name': 'Sachin', 'age': 32, 'runs': 120, 'oppn': 'srilanka', 'venue': 'chepauk'}
print(f"player :{player}")

k = player.keys()
print(k)

print("-" * 60)
for k in player.keys():
    print(k + " => " + str(player[k]))

print("values".center(60, "-"))

player = {'name': 'Sachin', 'age': 32, 'runs': 120, 'oppn': 'srilanka', 'venue': 'chepauk'}
print(f"player :{player}")

v = player.values()
print(v)
print("-" * 60)

print("get".center(60, '-'))

player = {'name': 'Sachin', 'age': 32, 'runs': 120, 'oppn': 'srilanka', 'venue': 'chepauk'}
print(f"player :{player}")

print(f"Name :{player.get('name', 'Invalid Key, please enter a valid key.....')}")
print(f"Name :{player.get('nam', 'Invalid Key, please enter a valid key.....')}")

print("fromkeys".center(60, "-"))
# convert a list to a dictionary

cities = ['blr', 'che', 'hyd', 'mum', 'del', 'kol']
print(f"cities :{cities}")

res1 = dict.fromkeys(cities)
print(f"res1 :{res1}")

res2 = dict.fromkeys(cities, 21)
print(f"res2 :{res2}")

print("setdefault".center(60, "-"))
# setdefault = will allow us to add new key value, never allow us to modify
player = {'name': 'Sachin', 'age': 32, 'runs': 120, 'oppn': 'srilanka', 'venue': 'chepauk'}
print(f"player :{player}")

player.setdefault("name", "Tendulkar")
player.setdefault("runs", 50)

player.setdefault("year", 2005)
player.setdefault("country", "India")

print("-" * 60)
print(f"player :{player}")

