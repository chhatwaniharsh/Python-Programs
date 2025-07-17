class Employee:
    def assign(self,i,n,s):
        self.eid=i
        self.name=n
        self.salary=s
    def show(self):
        print(f"Employee ID : {self.eid}")
        print(f"Employee Name : {self.name}")
        print(f"Employee Salary : {self.salary}")
e1=Employee()
e2=Employee()

e1.assign(1,"ABC",85000)
e2.assign(2,"DEF",75000)

emp_list = [e1,e2]
for i in emp_list:
    i.show()
    print()
