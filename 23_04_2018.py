def printme(str):
    print(str)
    
printme("This is the first function")
printme("Again calling the same function")


employee = {"Alex":1500, "John":2600, "Tia5":3500}
def test(employee):
    new ={"Ravi":1293, "Max":1331, "Jain":1514}
    employee.update(new)
    print("Inside the function:",employee)
    return
test(employee)
print("Outside the function:",employee)


def changeme( mylist ): 
   "This changes a passed list into this function" 
   print ("Values inside the function before change: ", mylist) 
   mylist[2]=50 
   print ("Values inside the function after change: ", mylist)
   return 
mylist = [10,20,30] 
changeme( mylist ) 
print ("Values outside the function: ", mylist)
