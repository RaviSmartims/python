"""fo= open("fooi.txt","rw+")
print("Name of the file:", fo.name)

line=fo.readlines()
print("Read Line: %s" % (line))
fo.seek(0,0)
line = fo.readline()
print("Read Line: %s" % (line))
fo.close()"""


"""fo= open("fooi.txt","r+")
print("Name of the file:", fo.name)

line=fo.readline()
print("Read Line: %s" % (line))
pos=fo.tell()
print("current position: ", pos)
fo.close()"""


"""fo= open("fooi.txt","r+")
print("Name of the file:", fo.name)

line=fo.readline()
print("Read Line: %s" % (line))
fo.truncate()
pos = fo.readlines()
print("Read Line: %s" % (pos))
fo.close()"""

"""fo= open("fooi.txt", "r+")
print("Name of the file:",fo.name)
str="This is 6th line"
fo.seek(0,2)
line= fo.write(str)
fo.seek(0,0)
for index in range(5):
    line=next(fo)
    print("Line No %d - %s" % (index,line))
fo.close()"""



"""fo=open("fooi.txt","r+")
print("Name of the file:", fo.name)
seq = ["This is 4th line\n", "This is the 5th line"]
fo.seek(0,2)
line = fo.writelines(seq)
fo.seek(0,0)
for index in range(5):
    line=next(fo)
    print("Line No %d - %s" % (index,line))
fo.close()"""

"""import os, sys 
ret = os.access("/tmp/foo.txt", os.F_OK) 
print ("F_OK - return value %s"% ret)  
ret = os.access("/tmp/foo.txt", os.R_OK) 
print ("R_OK - return value %s"% ret) 
ret = os.access("/tmp/foo.txt", os.W_OK) 
print ("W_OK - return value %s"% ret)  
ret = os.access("/tmp/foo.txt", os.X_OK) 
print ("X_OK - return value %s"% ret)"""


import os, sys 
os.chdir("/var/www/html" )  
print ("Current working dir : %s" % os.getcwd())  
fd = os.open( "/tmp", os.O_RDONLY )   
os.fchdir(fd) 
print ("Current working dir : %s" % os.getcwd()) 
os.close( fd )



