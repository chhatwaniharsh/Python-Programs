class Student:
    def add(self,i,n,a,m):
        self.sid=i
        self.name=n
        self.age=a
        self.marks=m
    def show(self):
        print("-------------------------------")
        print("Student ID :",self.sid)
        print("Student Name :",self.name)
        print("Student Age :",self.age)
        print("Student Marks :",self.marks)
        print("-------------------------------")
    def update(self):
        sid = int(input("Enter Student ID to update: "))
        for s in l1:
            if s.sid == sid:
                s.name = input("Enter new Student Name : ")
                s.age = int(input("Enter new Student Age : "))
                s.marks = float(input("Enter new Student Marks : "))
                print("Student record updated.")
                return
        print("Student ID not found.")
    def delete(self):
        sid = int(input("Enter Student ID to delete : "))
        for s in l1:
            if s.sid == sid:
                sid=sid-1
                del l1[sid]
                print("Student record deleted.")
                return
        print("Student ID not found.")

obj=Student()
l1=[]
ch=0
while ch!=5:
    ch=int(input("Enter Your Choice\n1.Add Student\t2.Update Student\n3.Delete Student\t4.Show Students\n5.Exit : "))
    if ch==1:
        sid=int(input("Enter Student ID : "))
        name=input("Enter Student Name : ")
        age=int(input("Enter Student Age : "))
        marks=float(input("Enter Student Marks : "))
        s1=Student()
        s1.add(sid,name,age,marks)
        l1.append(s1)
    elif ch==2:
        obj.update()
    elif ch==3:
        obj.delete()
    elif ch==4:
        if not l1:
            print("No records available")
        for i in l1:
            i.show()
    elif ch==5:
        print("Exiting...")
    else:
        print("Please Enter Valid Choice!")
