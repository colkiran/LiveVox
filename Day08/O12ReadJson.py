
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





