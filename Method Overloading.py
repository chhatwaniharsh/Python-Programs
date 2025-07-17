from multipledispatch import dispatch

class MyClass:
    @dispatch(int,float)
    def add(self,a,b):
        ans=a+b
        print(ans)

    @dispatch(float,float)
    def add(self,a,b):
        ans=a+b
        print(ans)

myobj=MyClass()
myobj.add(10.2,20.5)
myobj.add(1,1.2)
