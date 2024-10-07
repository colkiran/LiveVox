
from threading import Thread

class Player:

    def get_runs(self, n):
        for i in range(5):
            print("Hello World")


    @classmethod
    def test(cls, x):
        for i in range(x):
            print("Greetings.....")


    @staticmethod
    def fun(y):
        for i in range(y):
            print("Welcome")


p1 = Player()

t1 = Thread(target=p1.get_runs, args=(5, ))
t1.start()

t2 = Thread(target=Player.test, args=(3, ))
t2.start()

t3 = Thread(target=Player.fun, args=(3, ))
t3.start()
