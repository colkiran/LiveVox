
list1 = ['a', 'b', 'c', 'd', 'e']
print(f"list1 :{list1}")

iterObj = list1.__iter__()

while True:
    try:
        elem = next(iterObj)        # same as iterObj.__next__()
        print(elem)
    except StopIteration:
        break

