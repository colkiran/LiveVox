"""
thread identifier = unique id within a python process assigned by Python Interpreter, it is a positive integer and read-only stored in a instance variable ident

native identifier - assigned by operating system and property name is native_id

NOTE - ident and native_id are same - in the sense their name will be the same but completely different identifiers

PID = process id - main program

"""


from threading import Thread, current_thread
import os

def display():
    for i in range(4):
        print("Hello World")

def show():
    for i in range(3):
        print("Welcome")

t1 = Thread(target=display)
t2 = Thread(target=show)

print(t1.name)
print(t2.name)

t1.name = "Mike"
print(t1.name)

# print(t1.getName())
# print(t2.getName())
# t1.setName("Mike")

print("-" * 60)

print(current_thread().name)
# change the name of the main thread
# current_thread().name = "Mike_Main"
# print(current_thread().name)

print("-" * 60)
t1.start()
print(t1.ident)
print(t1.native_id)
print(os.getpid())