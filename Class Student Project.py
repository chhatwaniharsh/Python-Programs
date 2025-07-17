class Student:
    id=0
    name=""
    age=0
    marks=0
    def add(self,i,n,a,m):
        self.id=i
        self.name=n
        self.age=a
        self.marks=m
    def show(self):
        print("Student ID :",self.id)
        print("Student Name :",self.name)
        print("Student Age :",self.age)
        print("Student Marks :",self.marks)
    def update(self,i,n,a,m):
        self.id=i
        self.name=n
        self.age=a
        self.marks=m
    def delete(self):
        self.id=0
        self.name=""
        self.age=0
        self.marks=0
        
s1=Student()

ch=0
while ch!=5:
    ch=int(input("\nEnter Student Choice\n1.Insert Data, 2.Update data, 3.Delete Data, 4.Show Data, 5.Exit : "))
    if ch==1:
        sid=int(input("Enter Student ID : "))
        sname=input("Enter Student Name : ")
        sage=int(input("Enter Student Age : "))
        sm=int(input("Enter Student Marks : "))
        s1.add(sid,sname,sage,sm)
        print("Data Inserted")
    elif ch==2:
        sid=int(input("Enter Student ID : "))
        sname=input("Enter Student Name : ")
        sage=int(input("Enter Student Age : "))
        sm=int(input("Enter Student Marks : "))
        s1.update(sid,sname,sage,sm)
        print("Data Updated")
    elif ch==3:
        s1.delete()
        print("Data Deleted")
    elif ch==4:
        s1.show()
    elif ch==5:
        print("Exiting...")
    else:
        print("Enter Valid Choice")
    
