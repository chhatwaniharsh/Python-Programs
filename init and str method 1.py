class MyClass:
    pass
myobj=MyClass()
print(myobj)

print()

class OtherClass:
    def __init__(self):
        print("__init__ called")
    def __str__(self):
        print("__str__ called")
        return "Hello returned from str"

otherobj=OtherClass()
print(otherobj)
