
glbx = 100

def fun(n):                 # n is a local variable
    global glbx             # do not assign any value in this line
    print(f"n :{n}")
    y = 50
    # y = y + glbx
    print(f"y :{y}")

    # print the value of glbx
    glbx = 500
    print(f"inside fun :{glbx}")
    print(f"inside fun :{id(glbx)}")


print(f"before  :{glbx}")
print(f"id before :{id(glbx)}")

fun("hello")

print(f"after :{glbx}")
print(f"id after :{id(glbx)}")
