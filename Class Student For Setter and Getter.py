class Student:
    __rn = 0
    __name = ""
    __marks = 0.0

    def setRn(self,r):
        self.__rn = r
    def getRn(self):
        return self.__rn
    def setName(self,n):
        self.__name = n
    def getName(self):
        return self.__name
    def setMarks(self,m):
        self.__marks = m
    def getMarks(self):
        return self.__marks

s1=Student()
print(s1.getRn())
print(s1.getName())
print(s1.getMarks())
print()

s1.setRn(36)
s1.setName("ABC")
s1.setMarks(95.8)

print(s1.getRn())
print(s1.getName())
print(s1.getMarks())
