from threading import Thread

def display():
    for i in range(4):
        print("Welcome")

def show():
    for i in range(4):
        print("Lets start the program.....")


t1 = Thread(target=display)
t2 = Thread(target=show)

t1.start()
# t1.join()

t2.start()
t2.join()

for i in range(4):
    print("Hello World")