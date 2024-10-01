class Employee:

    def __init__(self, name):
        self.__name = name          # private variable
        # self._name = name           # protected
        self.fname = "Ben"
        self.tech = ['C++', 'Dotnet', "Sharepoint", 'Biztalk Server', 'Dynamics',
                     'Sql Server', 'Anglar JS', 'React JS']
    
    def __str__(self):
        return self.__name + " - " + ", ".join([t for t in self.tech])



emp1 = Employee("Ruben")
print(emp1)

print("-" * 60)

print(emp1.__dict__)

print("-" * 60)
print(f"Name : {emp1._Employee__name}")

emp1._Employee__name = "Peter"

print("-" * 60)

print(emp1.__dict__)

print("-" * 60)

print(emp1.fname)
