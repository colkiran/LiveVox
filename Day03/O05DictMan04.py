

print("copy".center(60, "-"))

emp1 =  {'empid' :1211, 'empname' :'Jack', 'age' :32, 'desig' :'TL', 'dept': 'finance', 'salary': 65000}

print(f"emp1 before :{emp1}")

# copy emp1 to emp2

emp2 = emp1             # shallow copy - data is copied with the address

print(f"emp2 before :{emp2}")

emp2['loc'] = 'MG Road'
emp2['gender'] = 'Male'

print(f"emp2 after :{emp2}")
print(f"emp1 after :{emp1}")

print("=" * 60)
print("=" * 60)

emp3 = {'empid' :1211, 'empname' :'Jack', 'age' :32, 'desig' :'TL', 'dept': 'finance', 'salary': 65000}

print(f"emp3 before :{emp3}")

# copy emp3 to emp4

emp4 = emp3.copy()

print(f"emp4 before:{emp4}")

emp4['loc'] = 'MG Road'
emp4['gender'] = 'Male'

print("-" * 60)
print(f"emp4 after :{emp4}")
print("-" * 60)
print(f"emp3 after :{emp3}")

print("=" * 60)
print("=" * 60)


emp5 =  {'empid' :1211, 'empname' :'Jack', 'age' :32, 'desig' :{'HP': 'FE', 'TCS': 'SFE', 'IBM' :'TL'}, 'dept': 'finance', 'salary': 65000}

print(f"emp5 before :{emp5}")

# copy emp5 to emp6
emp6 = emp5.copy()

print(f"emp6 before :{emp6}")

emp6['desig']['cts'] = "Mgr"
emp6['desig']['wipro'] = "Sr. Mgr"

print("-" * 60)

print(f"emp6 after :{emp6}")
print("-" * 60)

print(F"emp5 after :{emp5}")

print("=" * 60)
print("=" * 60)

emp7 =  {'empid' :1211, 'empname' :'Jack', 'age' :32, 'desig' :{'HP': 'FE', 'TCS': 'SFE', 'IBM' :'TL'}, 'dept': 'finance', 'salary': 65000}

print(f"emp7 before :{emp7}")

# emp7 to emp8
from copy import deepcopy
emp8 = deepcopy(emp7)

print(f"emp8 before {emp8}")
emp8['desig']['cts'] = "Mgr"
emp8['desig']['wipro'] = "Sr. Mgr"

print(f"emp8 after :{emp8}")
print(f"emp7 after :{emp7}")
