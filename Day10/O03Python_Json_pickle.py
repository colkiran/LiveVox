
"""
JSON Module
  a. using json module we can serialize and deserialize several python types like
    bool, int, string, float, dict, list, tuple, none etc

  b. it is a very good choice for interoperability among different languages

"""
import json

# JSON String
data = {'name' :'sachin', 'age' :30, 'city' :'mumbai'}

# Serialization using Json
json_objects = json.dumps(data)
print(json_objects)
print("Serialization Completed")
print(type(json_objects))


print('-' * 60)
# convert the string into python dictionary
player = json.loads(json_objects)
print(player)
print("Desialization Completed")
print(type(player))
