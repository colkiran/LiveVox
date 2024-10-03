
"""
open a file writing - if the file already exists then delete contents of the file and write newly into the file. if the file does not exist then create a new file and write into the file
"""

FW = open("myfile.txt", "w")

# txt = input("Enter the contents of the file :")
# FW.write(txt)

l1 = "This is the first line.\n"
l2 = "This is the second line. \n"
l3 = "This is the last line. \n"

FW.writelines([l1, l2, l3])

FW.close()

