import time

def fun():
    print("Function going to sleep")
    time.sleep(2)
    print("Fuction just woke up....")

print("Function called.....")
st = time.perf_counter()
fun()
fun()
fun()
et = time.perf_counter()
print("Copleted execution of function.......")
print(f"The total time taken :{round(et - st, 2)}")