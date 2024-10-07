
"""
Python provides three different ways to serialize and deserialize objects


1. Marshal Module
2. Pickle Module
3. Json Module
4. Shelve

Marshal Module :-
  a. it is the oldest module
  b. it is not recomended
  c. mainly used by interpreter
  d. python maintainer can modify the format in backward compatible way

"""

import marshal

data = {'name' :'sachin', 'age' :34, 'city' :'mumbai'}

# dumps - return byte object stored in variable 'bytes'
bytes = marshal.dumps(data)
print("After Serialization :", bytes)

print("-" * 60)

# loads() converts bytes objects into values
new_data = marshal.loads(bytes)
print("After Deserialization :", new_data)
