class Student:
    def __init__(self,r,n,m):
        self.rn=r
        self.name=n
        self.marks=m
    def __str__(self):
        return f"RN={self.rn}, NAME={self.name}, MARKS={self.marks}"

s1=Student(1,"abcd",10)
s2=Student(2,"defg",20)
s3=Student(3,"ghij",30)
student_list=[s1,s2,s3]

print(student_list)
for stud in student_list:
    print(stud)

                                            
print(student_list[0])
print(student_list[0].rn)
print(student_list[0].name)
print(student_list[0].marks)

print(student_list[1])
print(student_list[1].rn)
print(student_list[1].name)
print(student_list[1].marks)

print(student_list[2])
print(student_list[2].rn)
print(student_list[2].name)
print(student_list[2].marks)
