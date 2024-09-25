
emp = {
    'emp1': {'empid' :1211, 'empname' :'Jack', 'age' :32, 'desig' :'TL', 'dept': 'finance', 'salary': 65000, 'location': 'Whitefield'},
    'emp2': {'empid' :2225, 'empname' :'Tina', 'age' :42, 'desig' :'MGR', 'dept': 'MKT', 'salary': 70000, 'location': 'Electronic City'},
    'emp3': {'empid' :3443, 'empname' :'Colin', 'age' :28, 'desig' :'SE', 'dept': 'IT', 'salary': 45000, 'location': 'Manyata'}
}

print(f"emp :{emp}")
print("-" * 60)

print(f"emp1 :{emp['emp1']}")
print("-" * 60)

print(f"emp2 :{emp['emp2']}")
print("-" * 60)

print(f"emp3 :{emp['emp3']}")
print("-" * 60)

for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 60)

print("pop".center(60, "-"))
emp1 = {'empid' :1211, 'empname' :'Jack', 'age' :32, 'desig' :'TL', 'dept': 'finance', 'salary': 65000, 'location': 'Whitefield'}

print(f"emp1 :{emp1}")
print(type(emp1))

res = emp1.pop('age')
print(f"res :{res}")

res = emp1.pop('location')
print(f"res :{res}")

# res = emp1.pop()
# print(f"res :{res}")

print(f"emp1: {emp1}")

print("popitem".center(60 ,"-"))

emp1 = {'empid' :1211, 'empname' :'Jack', 'age' :32, 'desig' :'TL', 'dept': 'finance', 'salary': 65000, 'location': 'Whitefield'}

print(f"emp1 :{emp1}")

res = emp1.popitem()
print(f"res :{res}")

res = emp1.popitem()
print(f"res :{res}")

res = emp1.popitem()
print(f"res :{res}")

print(f"emp1 :{emp1}")

print("update".center(60, "-"))

emp1 = {'empid' :1211, 'empname' :'Jack', 'age' :32, 'desig' :'TL', 'dept': 'finance', 'salary': 65000}

print(f"emp1 :{emp1}")
print()
print("-" * 60)
print()
emp2 = {'empid' :2225, 'empname' :'Tina', 'age' :42, 'desig' :'MGR', 'dept': 'MKT',  'location': 'Electronic City'}

print(f"emp2 :{emp2}")

print()
print("-" * 60)
print()

# update the values of emp1 from emp2
emp1.update(emp2)

print(F"emp1 :{emp1}")