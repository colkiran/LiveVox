
import json

FL = open("books.json", "r")
jsonFR = json.load(FL)

# print(jsonFR)

for book in jsonFR['books']:
    print(book['name'])
    print("-" * len(book['name']))
    for k, v in book.items():
        print(k, "=>", v)
    print("-" * 60)

print("-" * 60)
# data is enclosed in single quotes
empdata = '{"name": "Micheal", "age": 35, "desig": "MGR", "dept": "finance"}'
print(f"empdata : {empdata}")
print(type(empdata))

# loads - json string document into python dictionary
print("-" * 60)
res = json.loads(empdata)
print(f"res :{res}")
print(type(res))

for k, v in res.items():
    print(k, "=>", v)


