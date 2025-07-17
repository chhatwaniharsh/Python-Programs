class MyClass:
    x=10
    _y=20
    __z=30

myobj=MyClass()
print(myobj.x)      #10
print(myobj._y)     #20
#print(myobj.__z)   #ERROR
