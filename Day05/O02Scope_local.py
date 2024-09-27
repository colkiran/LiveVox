
def fun(x):             # x = local variable
    global z
    print(f"x :{x}")
    z = 250
    y = 500
    print(f"y :{y}")

fun(100)

# print(y)
print(f'z :{z}')
# z = 500
#
# print(f'z :{z}')

print("-" * 60)


lst = list(range(1, 11))

for i in range(1, len(lst)):
    print(lst[i],  end = " ")
print()

print("After :", i)
print(k)
