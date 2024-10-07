"""
count of current running thread
details of all threads

is_alive()  - checks if the thread is running or not
main_thread() - returns main threads details
active_count() - Number of running threads
enumerate() - list of all running threads
get_native_id() - know native id of thread

"""

from threading import Thread, main_thread, active_count, enumerate, get_native_id
import os

def display():
    print("ID :", get_native_id())
    print("Main Thread details :", main_thread())
    for i in range(4):
        print("Hello World")

def show():
    for i in range(3):
        print("Welcome")

t1 = Thread(target=display)
print("Before :", t1.is_alive())
t1.start()

print("ID :", get_native_id())
# print("Number of threads :", active_count())

print("Thread details :", enumerate())


print("After :", t1.is_alive())
