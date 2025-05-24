class GreatSmall:
    def check(self,a,b):
        if a>b:
            print(f"{a} is greater than {b}")
        elif a<b:
            print(f"{a} is Smaller than {b}")
        else:
            print("Both are equal")
gs=GreatSmall()
x=int(input("Enter Number 1 : "))
y=int(input("Enter Number 2 : "))
gs.check(x,y)
