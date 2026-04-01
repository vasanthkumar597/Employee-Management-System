class Employee:
    company_name="google"
    total_employees=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.total_employees+=1
    def show_info(self):
        print(f"Company name: {self.company_name}")
        print(f"Employee name:{self.name}")
        print(f"Salary : {self.salary}")
        print(f"Tax : {Employee.calculate_tax(self.salary)}")
        print("===========================")
    @classmethod
    def change_company(cls,new_name):
        cls.company_name=new_name
    @staticmethod
    def calculate_tax(salary):
        return salary*0.10
class manager(Employee):
    def __init__(self,name,salary,bonus):
        super().__init__(name,salary)
        self.bonus=bonus
    def show_info(self):
        super().show_info()
        print(f"Bonus:{self.bonus}")
        print("=========================")
    @staticmethod
    def calculate_bonus(salary):
        return salary*0.15
class developer(Employee):
    def __init__(self,name,salary,allowence):
        super().__init__(name,salary)
        self.allowence=allowence
    def show_info(self):
        super().show_info()
        print(f"Project allowence : {self.allowence}")
    @staticmethod
    def calculate_allowence(salary):
        return salary*0.08  
employees=[]
num=int(input("how many employees want to add : "))
for i in range(num):
    print(f"Employee details {i+1}")
    choice=input("which position (manager/developer): ").lower()
    if choice=="manager":
        name=input("enter the name: ")
        salary=int(input("enetr the salary: "))
        bonus=manager.calculate_bonus(salary)
        print(f"Bonus added :{bonus}")
        emp=manager(name,salary,bonus)
        employees.append(emp)
    elif choice=="developer":
        name=input("enter the name: ")
        salary=int(input("enetr the salary: "))
        allowence=developer.calculate_allowence(salary)
        print(f"Project allowence : {allowence}")
        emp=developer(name,salary,allowence)
        employees.append(emp)
    else:
        print("invalid position ,sklipping the employeee")
    print("============================================")
choice=input("do you want to change company : ").lower()

if choice =="yes":
    new_name=input("enter the company name: ")
    Employee.change_company(new_name)
else:
    None
print("----------all employee details------------------")
for emp in employees:
    emp.show_info()


print(f"total employees : {Employee.total_employees}")










    