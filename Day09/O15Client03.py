
import requests
import json

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "getproduct/coke")

res = response.json()

for k, v in res.items():
    print(k, "=>", v)

print("put".center(60, "-"))

response = requests.put(BASE + "getproduct/coke", data={'cat': 'baverage'})

res = response.json()

for k, v in res.items():
    print(k, "=>", v)

print("Patch".center(60, "-"))
data = {'price': 5000}

response = requests.patch(BASE + "getproduct/coke", json=json.dumps(data))
res = response.json()

for k,v in res.items():
    print(k, "=>", v)

print("Post".center(60, "-"))
fanta = {'item': '100 ml bottle', 'price': 20, 'qty': '300 crates'}

response = requests.post(BASE + "getproduct/fanta", json=json.dumps(fanta))
res = response.json()

for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 60)

print("Delete".center(60, "-"))

response = requests.delete(BASE + "getproduct/thumbs_up")
res = response.json()

for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 60)