
import threading

print(threading.current_thread())

print("Main Thread Name :", threading.current_thread().name)
print("PID :", threading.current_thread().ident)
print("Thread Status :", threading.current_thread().is_alive())


# print main thread name

