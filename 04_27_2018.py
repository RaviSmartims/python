"""print(1 + 2)
print(int.__add__(1,2))
print(str.__add__("a", "b"))"""


 
"""class Employee:
    def __init__(self,first,last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + "@company.com"

    def fullname(self):
        return "{} {}".format(self.first,self.last)


emp1 = Employee("Ravi", "Reddy")

print(emp1.first)
print(emp1.email)
print(emp1.fullname())"""

"""-----"""

"""class Employee:
    def __init__(self,first,last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + "@company.com"

    def fullname(self):
        return "{} {}".format(self.first,self.last)


emp1 = Employee("Ravi", "Reddy")

emp1.first = "Sunil"

print(emp1.first)
print(emp1.email)
print(emp1.fullname())"""

"""-----"""


"""class Employee:
    def __init__(self,first,last):
        self.first = first
        self.last = last        

    def email(self):
        return "{} {}@company.com".format(self.first,self.last)

    def fullname(self):
        return "{} {}".format(self.first,self.last)


emp1 = Employee("Ravi", "Reddy")

emp1.first = "Sunil"

print(emp1.first)
print(emp1.email())
print(emp1.fullname())"""

"""----as a decorator---"""

class Employee:
    def __init__(self,first,last):
        self.first = first
        self.last = last        
    @property
    def email(self):
        return "{} {}@company.com".format(self.first,self.last)

    def fullname(self):
        return "{} {}".format(self.first,self.last)


emp1 = Employee("Ravi", "Reddy")

emp1.first = "Sunil"

print(emp1.first)
print(emp1.email)
print(emp1.fullname())




