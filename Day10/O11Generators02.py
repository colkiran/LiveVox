
def fun():
    n = 1
    print("apples from ooty")
    yield n
    n += 9
    print("oranges from kanpur")
    yield n
    n += 10
    print("Grapes from hubli")
    yield n



res = fun()
print(type(res))
# print(f"res :{res}")

print(res.__next__())
print("code....")
print(res.__next__())
print("code....")
print(res.__next__())

print("-" * 60)

def fun():
    for i in range(1, 20, 5):
        yield i

res = fun()
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())

print("-" * 60)

for x in fun():
    print(x)