

"""
open a file in append - if the file already exists then appends the contents into the file without disturbing the old contents. if the file does not exist then create a new file and write into the file
"""

FA = open("myfile.txt", "a")

txt = input("Enter the contents of the file :")

FA.write(txt + "\n")

FA.close()

