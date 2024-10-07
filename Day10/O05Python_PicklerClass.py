"""
pickle has a Pickler class which has the dump method
pickle has a Unpickler class that reads the data from the file
"""

from pickle import Pickler, Unpickler

f1 = open("pickled.txt", "wb")
dct = {"name": "sachin", "age": 45, "Gender": "Male", "city": 'mumbai'}
Pickler(f1).dump(dct)
f1.close()


f2 = open("pickled.txt", "rb")
dct = Unpickler(f2).load()
print(dct)
f2.close()