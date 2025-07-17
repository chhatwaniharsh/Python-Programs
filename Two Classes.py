class MyClass:
    x=10
    def m1(self):
        print("m1 method of MyClass called")

class OtherClass:
    y=20
    def m2(self):
        print("m2 method of OtherClass called")

myobj=MyClass()
print(myobj.x)
myobj.m1()

otherobj=OtherClass()
print(otherobj.y)
otherobj.m2()
