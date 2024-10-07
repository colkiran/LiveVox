"""
Advantage of using inheritance is we can get the data used in the thread

"""

from threading import Thread
from time import sleep

courses  = ['Python', 'Deep Learining', "Machine Learning", "React JS"]

class MyCBT(Thread):

    def __init__(self, Flag):
        # execute the thread class ctor to start the necessary threads
        super().__init__()
        print("MyCBT Ctor.......")
        self.student_offer = Flag

    def fastTrack(self):
        print("This is a Fast track course.....")

    def run(self):
        a = 10
        b = 20
        self.fastTrack()

        if self.student_offer:
            print("Student offer is on......")

        for course in courses:
            print(f"{course} Joined......")
            sleep(2)
            print(f"{course} completed......")
        self.temp = a + b

t1 = MyCBT(False)
t1.start()
sleep(10)
print(t1.temp)



for i in range(4):
    sleep(1)
    print("Registered for the course")





"""
def upgrade(course):
    print(f"{course} Joined......")
    sleep(3)
    print(f"{course} completed......")
"""