class Employee:
    num_of_emps = 0
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        
        Employee.num_of_emps += 1

emp1 = Employee("Ravi", "Reddy", 50000)
emp2 = Employee("Sunil", "Reddy", 60000)

print(Employee.num_of_emps)

class Employee:
    num_of_emps = 0
    raise_amt = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        
        Employee.num_of_emps += 1
        
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount

emp1 = Employee("Ravi", "Reddy", 50000)
emp2 = Employee("Sunil", "Reddy", 60000)

Employee.set_raise_amt(1.05)

#print(Employee.num_of_emps)
print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)


