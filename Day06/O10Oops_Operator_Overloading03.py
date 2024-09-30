
class Employee:

    def __init__(self, name):
        self.name = name
        self.tech = ['C++', "Java", 'J2EE', 'Spring', 'Hibernate', 'AngularJS', 'ReactJS']

    def __str__(self):
        return self.name + " - " + ' '.join([t for t in self.tech])

    def __iter__(self):
        return iter(self.tech)

    def append(self, val):
        self.tech.append(val)

    def __getitem__(self, idx):
        return self.tech[idx]

    def __setitem__(self, idx, val):
        self.tech[idx] = val


emp1 = Employee("Jack")
print(emp1)

print("-" * 60)
print([e for e in emp1])

print("-" * 60)
emp1.append("Python")

print("-" * 60)
print([e for e in emp1])

print("-" * 60)
x = emp1[4]
print(f"x :{x}")

print("-" * 60)
emp1[2] = "JSP"

print("-" * 60)
print([e for e in emp1])



