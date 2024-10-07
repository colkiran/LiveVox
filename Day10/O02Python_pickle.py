"""
Pickle Module
  a. it serializes python objects into binary formats
  b. it is faster and also works with customized objects
  c. better choice for serialization and deserialization of python objects
"""
import pickle

data = {'name' :'sachin', 'age' :30, 'city' :'Mubai'}

with open("data.pickle", "wb") as FW:
    pickle.dump(data, FW)
    print("completed pickling.......")

with open("data.pickle", "rb") as FL:
    print("Unpickling the data :")
    player = pickle.load(FL)
    print(player)

