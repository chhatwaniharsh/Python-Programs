class Employee:
    def __init__(self,i,n,s):
        self.eid=i
        self.name=n
        self.salary=s
    def __str__(self):
        return f"Employee ID={self.eid}, Employee Name={self.name}, Employee Salary={self.salary}"
e1=Employee(1,"ABC",45000)
e2=Employee(2,"DEF",40000)
e3=Employee(3,"GHI",50000)
emp_list=[e1,e2,e3]
for emp in emp_list:
    print(emp)
