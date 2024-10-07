
from threading import Thread, current_thread
import time

def fun():
    print(f"Function going to sleep.. {current_thread().name}")
    time.sleep(2)
    print(f"Fuction just woke up.... {current_thread().name}")

print("Function called.....")
st = time.perf_counter()
t1 = Thread(target=fun)
t2 = Thread(target=fun)
t3 = Thread(target=fun)

print(t1.name)
print(t2.name)
print(t3.name)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

# thread id will be assigned when the thread starts

et = time.perf_counter()
print("Copleted execution of function.......")
print(f"The total time taken :{round(et - st, 2)}")

for i in range(5):
    print("Hello World")
