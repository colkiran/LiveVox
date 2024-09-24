
st = "hello world"
print(f"st :{st}")
print(type(st))

# print(dir(st))
print("-" * 60)
# strings are stored like a list or an array
# indexing starts from 0 (zero)
print(f"st[0]  :{st[0]}")
print(f"st[6]  :{st[6]}")
print(f"st[10] :{st[10]}")

print("-" * 60)
# slicing
print(f"st[0:5]  :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:11] :{st[0:11]}")
print(f"st[0:]   :{st[0:]}")
print(f"st[:11]  :{st[:11]}")
print(f"st[:]    :{st[:]}")

print("-" * 60)
# reverse indexing
print(f"st[-1] :{st[-1]}")
print(f"st[-5] :{st[-5]}")
print(f"st[-11]:{st[-11]}")

print("-" * 60)
# slicing
print(f"st[-1:-6:-1] :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[-1::-1]    :{st[-1::-1]}")
print(f"st[:-12:-1]   :{st[:-12:-1]}")
print(f"st[::-1]      :{st[::-1]}")

# unsing indexing find if  the string is a palindrome

st = "malayalam"
print("Palindrome" if st[:] == st[::-1] else "Not a palindrome")
# st[-1::] == st

print("-" * 60)
# manipulate a string

# st = "hello world"
# strings are immutable
# print(f"st[0] :{st[0]}")
# st[0] = "H"

# find,  replace
st1 = "hello world"
st2 = "the quick brown fox jumps over the lazy dog"

pos = st1.find("l")
print(f"index :{pos}")

# pos = st1.find("l", 5)    # hard coding
pos = st1.find("l", st1.find("l") + 1)
print(f"index :{pos}")

pos = st1.find("l", st1.find("l", st1.find("l") + 1) + 1)
print(f"index :{pos}")

print("-" * 60)
pos = st2.find("the")
print(f"index :{pos}")

pos = st2.find("the", st2.find("the") + 1)
print(f"index :{pos}")

print("replace".center(60, "-"))
st1 = "hello world"
st2 = "the quick brown fox jumps over the lazy dog"

print(f"st1 :{st1}")

print("-" * 60)
res = st1.replace("l", "L")
print(f"New String :{res}")
res = st1.replace("l", "L", 2)
print(f"New String :{res}")
res = st1.replace("l", "L", 1)
print(f"New String :{res}")

