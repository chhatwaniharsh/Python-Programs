class Student:
    rn=0
    name=""
    marks=0.0
    def __init__(self,r,n,m):
        self.rn=r
        self.name=n
        self.marks=m
    def __str__(self):
        return f"RN={self.rn},NAME={self.name},MARKS={self.marks}"
s1=Student(1,"abcd",10)
print(s1)
s2=Student(2,"defg",20)
print(s2)
