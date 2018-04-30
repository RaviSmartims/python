"""fo = open("foo.txt","wb")
print("Name of the file:", fo.name)
print("closed or not:", fo.closed)
print("Opening mode:", fo.mode)
fo.close()"""

"""print("Python is a interesting language")"""

"""x =input("something:")
something:10
x"""

"""fo = open("foo.txt", "wb")
print("Name of the file:",fo.name)

fo.close()"""


"""fo = open("foo.txt","w")
fo.write("Python is a great language.\n Yeah its great!!!\n")
fo.close()"""
"""fo= open ("foo.txt", "rt")
str = fo.read(10)
print("Read String is :", str)
fo.close()"""

"""#Open a file"""
fo = open("foo.txt","r+")
str = fo.read(10)
print("Read String is:" ,str)

"""#Check current position """
position= fo.tell()
print("Current file position:",position)

"""#Reposition pointer at the beginning once again"""

"""position = fo.seek(0,0)
str = fo.read(10)
print("Again read string is:", str)
fo.close()"""


import os
os.rename("test1.txt","test2.txt")















