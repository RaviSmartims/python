"""fo=open("foo.txt","wb")
print("Name of the file:",fo.name)
fo.close()"""


"""fo=open("foo.txt","wb")
print("Name of the file:",fo.name)
#Here it does nothing, but you can call it with read operation
fo.flush()
# Close opend file
fo.close()"""

"""fo=open("abcd.txt","wb")
print("Name of the file:", fo.name)
fid=fo.fileno()
print("File descriptor:",fid)
fo.close()"""

"""fo=open("abcd.txt","w")
print("Name of the file:",fo.name)
ret=fo.isatty()
print("Return value:",ret)
fo.close()"""

"""fo.txt =input(["C++","Java","Pyhon"])
fo=open("foo.txt", "r")
print("Name of the file:",fo.name)
for index in range(5):
    line=next(fo)
    print("Line No %d - %s" %(index,line))
    fo.close()"""

"""fo=open("foo.txt","rt")
print("Name of the file:",fo.name)
line= fo.readline()
print("Read Line:%s" %(line))
line=fo.readline(5)
print("Read Line: %s" %(line))
fo.close()"""


fo = open("foo.txt", "r+") 
print ("Name of the file: ", fo.name) 
line = fo.readlines() 
print ("Read Line: %s" % (line)) 
line = fo.readlines(2) 
print ("Read Line: %s" % (line)) 
fo.close() 




