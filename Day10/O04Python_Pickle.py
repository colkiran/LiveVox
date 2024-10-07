
"""
dump and load function of pickle module respectively to perform pickling and unpickling of data

dump function writes the pickled object to a file
load function unpickles data from file back to python object
"""

import pickle
FW = open("pickle.txt", "wb")
dct = {"name" :"Rahul", "age": 53, "Gender" :"Male", "City" :"Bangalore"}
pickle.dump(dct, FW)
FW.close()

FL = open("pickle.txt", "rb")
d1 =  pickle.load(FL)
print(d1)
FL.close()

