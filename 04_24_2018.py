#class Employee:
 #   def __init__(self,first,last,pay):
  #      self.first = first
  #      self.last = last
   #     self.pay = pay
        #self.email = email
    #    self.email = first + '.' +  last + '@company.com'

#emp_1 = Employee("Ravi", "Reddy", 50000)
#emp_2 = Employee("Sunil", "Reddy", 60000)

#print(emp_1.email)
#print(emp_2.email)

# If i want the full name i can do that coming out of the class and type

#print('{} {}'.format(emp_1.first, emp_2.last))

#instead of class seperately we can put that in classwe can do that calling the method

#class Employee:
    #def __init__(self,first,last,pay):
       # self.first = first
       # self.last = last
       # self.pay = pay
        #self.email = email
      #  self.email = first + '.' +  last + '@company.com'
    #def fullname(self):
     #       return '{} {}'.format(self.first, self.last)
        

#emp_1 = Employee("Ravi", "Reddy", 50000)
#emp_2 = Employee("Sunil", "Reddy", 60000)

#print(emp_1.email)
#print(emp_2.email)

#print(emp_2.fullname())

#---- Class Variables --


class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        #self.email = email
        self.email = first + '.' +  last + '@company.com'
    def fullname(self):
            return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * 1.04)
        

emp_1 = Employee("Ravi", "Reddy", 50000)
emp_2 = Employee("Sunil", "Reddy", 60000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)


