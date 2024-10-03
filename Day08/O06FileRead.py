"""
read is the default mode
if we open the file in read mode we can only read the contents of the file. If the file is not found then raises an exception - FileNotFoundError

 read - reads the entire content of the file
 read(args) - no of bytes can be specified - reads the contents depending on the no of bytes specified

readline = reads one line = one paragraph =>
readlines() - reads all the lines from the file and stores it in a list

"""


FL = open("data.txt", "r")

# st = FL.read(1000)
# st = FL.readline()

st = FL.readlines()
print(st)

# for line in st:
#     print(line)


FL.close()