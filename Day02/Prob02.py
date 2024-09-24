n = 0
for i in range(150, 50, -1):
    cntr = 0
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        n += 1
        print(i, end=" ")

print(f"\nThere are {n} prime numbers between 150 and 50")


age =19
print("Eligible" if age > 17 else "not eligible" if age < 10 else "Good")