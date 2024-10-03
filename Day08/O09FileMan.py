
FL = open("data.txt", "rb")

# pos = FL.seek(150, 0)         # 150 is calculated from the BOF
# print(f"Position :{pos}")
#
# pos = FL.seek(85, 1)
# print(f"Position :{pos}")
#
# pos = FL.seek(100, 2)
# print(f"Position :{pos}")

pos = FL.seek(350, 0)
print(f"Position :{pos}")

print("-" * 60)

pos = FL.seek(-230, 1)
print(f"Position :{pos}")

print("-" * 60)

pos = FL.seek(300, 1)
print(f"Position :{pos}")

print("-" * 60)

pos = FL.seek(-500, 2)
print(f"Position :{pos}")

print("-" * 60)

# error
# pos = FL.seek(-10, 0)
# print(f"Position :{pos}")



FL.close()