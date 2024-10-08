
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def doJob(self):
        pass

class Manager(Employee):

    def doJob(self):
        print("Managers Job.......")


class Developer(Employee):

    def doJob(self):
        print("Developers job.......")



def BankJob(emp):
    print("Bank job started.......")
    emp.doJob()
    print("Bank job ended........")
    print("-" * 60)


Mike = Manager()
Peter = Developer()

BankJob(Mike)           # will do the job of a manager

BankJob(Peter)          # will do the job of a developer

