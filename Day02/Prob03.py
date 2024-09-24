
print("maketrans".center(60, "-"))
st = "cat bat mat catbat rathat what"
print(f"st :{st}")
# length of a and b should be the same
a = "at"
b = "xy"

Tbl = st.maketrans(a, b)
print(Tbl)

res = st.translate(Tbl)
print(f"res :{res}")