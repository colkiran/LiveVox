
gname = "Sunil Gavaskar"

sports = ['cricket', 'tennis', 'football', 'hockey', 'badmiton', 'basketball', 'swimming']

runs = {'test': 18597, 'odi': 25450, 't20': 2500}


def greet(gnm):
    print(f"Greetings Mr.{gnm}, Welcome to the event.....")


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

# print("Module :",__name__)


if __name__ == "__main__":

    greet("Virat Kholi")

    print("-" * 60)

    emp1 = Employee("Ricard", 45000)
    print(emp1)


