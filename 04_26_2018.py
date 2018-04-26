 
    
#emp_str_1 = "John-Doe-70000"
#emp_str_2 = "Steve-Smith-30000"
#emp_str_3 = "Jane-Doe-90000"

    

#first,last,pay = emp_str_1.split('-')

#new_emp1 =first,last,pay

#print(new_emp1)

"""class Employee:
    raise_amt = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company.com"

    def fullname(self):
         return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10

dev1 = Developer("Ravi", "Reddy", 50000)
dev2 = Developer("Sunil", "Reddy",60000)

#print(Employee.fullname(dev1))
print(dev1.email)
print(dev2.email)

print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)"""


class Employee:
    raise_amt = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company.com"

    def fullname(self):
         return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self,first,last,pay, prog_lang):
        super().__init__(first,last,pay)
        """Employee.__init__(self,first,last,pay)"""
        self.prog_lang = prog_lang

class Manager(Employee):    
    def __init__(self,first,last,pay, employees=None):
        super().__init__(first,last,pay)
        """Employee.__init__(self,first,last,pay)"""
        if employees is None:
            self.employees = []
        else:
            self.employees =  employees
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
        
        
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->',emp.fullname())
       

dev1 = Developer("Ravi", "Reddy", 50000, "Pyhton")
dev2 = Developer("Sunil", "Reddy",60000, "Java")

mgr = Manager("Kalpana", "Reddy", 40000,[dev1])
print(mgr.email)
mgr.add_emp(dev2)
mgr.remove_emp(dev1)
mgr.print_emps()



#print(Employee.fullname(dev1))
#print(dev1.email)
#print(dev2.prog_lang)

"""print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)"""















    
