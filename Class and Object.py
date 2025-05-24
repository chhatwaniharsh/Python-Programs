var=10
def fun1():
    print("fun1 function starts")
    print("in the function fun1")
    print("fun1 function ends")

print(var)
fun1()
    
print()

class MyClass:
    var=36
    def m1(self):
        print("m1 method starts")
        print("in the method m1")
        print("m1 method ends")
obj=MyClass()
print(obj.var)
obj.m1()
