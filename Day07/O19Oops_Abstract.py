
from abc import ABC, abstractmethod

class Account(ABC):

    def withDraw(self):
        pass

    @abstractmethod
    def get_balance(self):
        print("hello world")


class Savings(Account):

    def withDraw(self):
        print("Amount successfully debited from the account.....")

    def get_balance(self):
        print("Balance in the account is ######.##")


class Current(Savings):

    def withDraw(self):
        print("Amount successfully debited from the account.....")

sav = Savings()
sav.withDraw()
sav.get_balance()

cur = Current()
