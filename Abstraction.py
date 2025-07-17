from abc import ABC,abstractmethod

class MyClass(ABC):
    @abstractmethod
    def m1(self):
        pass
    def m2(self):
        print("m2 of MyClass Called")
#m1=MyClass()   #TypeError

class ChildClass(MyClass):
    def m1(self):
        print("m1 of ChildClass Called")

c1=ChildClass()
c1.m1()
c1.m2()
