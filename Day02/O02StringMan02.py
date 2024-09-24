
st = "hello world"
print(f"st :{st}")

res = st.upper()
print(f"res :{res}")

print(st.isalpha())

print("-" * 60)

"""
maketrans and translate

maketrans - will change the text byte by byte - ascii format
ex - "we have an apple tree"  - replace all a's with x  = we hxve xn xpple tree

"""
print("maketrans".center(60, "-"))
st = "hello world"
print(f"st :{st}")
# length of a and b should be the same
a = "helowrd"
b = "HELOWRD"

Tbl = st.maketrans(a, b)
print(Tbl)

res = st.translate(Tbl)
print(f"res :{res}")
