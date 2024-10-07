
from threading import Thread, current_thread

class Bus:
    def __init__(self, name, available_seats):
        self.available_seats = available_seats

    def reserve(self, block_seats):
        print("Available seats :", self.available_seats)
        if self.available_seats >= block_seats:
            # ticket booking code goes here, update database
            print(f"{block_seats} is blocked by {current_thread().name}")
            self.available_seats -= block_seats
        else:
            print("Sorry all seats are blocked......")

bus1 = Bus("KPN", 2)

t1 = Thread(target=bus1.reserve, args=(1, ), name="Jack")
t2 = Thread(target=bus1.reserve, args=(2, ), name="Jill")
t1.start()
t2.start()