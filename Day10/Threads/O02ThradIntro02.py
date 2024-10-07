
from threading import Thread, current_thread

def fun(n, msg):
    print("t1 thread detais :", current_thread())
    for i in range(n):
        print(msg)

# t1 = Thread(target=fun, args=(4, "Hello World"))
t1 = Thread(target=fun, kwargs= {'n': 4, 'msg': "Hello World"})

t1.start()


for j in range(5):
    print("Welcome")

