class College:
    def clg(self):
        print("College Class")
class Department(College):
    def dept(self):
        print("Department Class")
class Branch(Department):
    def brc(self):
        print("Branch Class")
class Division(Branch):
    def div(self):
        print("Division Class")
class Student(Division):
    def stud(self):
        print("Student Class")
class Subject(Student):
    def sub(self):
        print("Subject Class")
sobj=Subject()
sobj.clg()
sobj.dept()
sobj.brc()
sobj.div()
sobj.stud()
sobj.sub()
