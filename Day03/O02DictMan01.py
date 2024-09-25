
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 60)
d2 = {'name': 'Sachin', 'age': 34, 'runs': 85, 'oppn': 'WI', 'venue': 'Sabina Park'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 60)
d3 = dict([('name', 'rahul'), ('age', 32), ('runs', 102), ('oppn', 'eng'), ('venue', 'lords')])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 60)
d4 = dict(name='Sourav', age=31, runs=145, oppn='pak', venue='toronto')
print(f"d4 :{d4}")
print(type(d4))

print("-" * 60)
# CRUD

# create
player = {'name': 'Sachin', 'age': 32, 'runs': 120, 'oppn': 'srilanka', 'venue': 'chepauk'}
print(f"player :{player}")

print("-" * 60)
# read
print(f"Name :{player['name']}")
print(f"Runs :{player['runs']}")

print("-" * 60)
for i in player:
    print(i, "=>", player[i])

print("-" * 60)
# update => 1. modify the exiting values, 2. add a new key value

print(f"player :{player}")
player['name'] = "Tendulkar"
player['venue'] = "Chinna Swamy"

player['year'] = 2003
player['avg'] = 65.5

print("-" * 60)
print(f"player :{player}")

print("-" * 60)
# delete
del player['age']
del player['oppn']
del player['avg']

print(f"player :{player}")

print("-" * 60)
print(dir(player))
