class Student:
    def assign(self,i,n,m):
        self.id=i
        self.name=n
        self.marks=m
    def show(self):
        print(f"Student Id : {self.id}")
        print(f"Student Name : {self.name}")
        print(f"Student Marks : {self.marks}")
s1=Student()
s2=Student()

s1.assign(1,"ABC",85)
s2.assign(2,"DEF",93)

stud_list=[s1,s2]
for i in stud_list:
    i.show()
    print()
