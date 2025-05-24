class GreatSmall:
    def check(self,a,b,c):
        if a>b and a>c:
            print(f"{a} is greater than {b} and {c}")
        elif a>b and a<c:
            print(f"{a} is greater than {b} but smaller than {c}")
        elif a<b and a>c:
            print(f"{a} is greater than {c} but smaller than {b}")
        elif a==b and a>c:
            print(f"{a} is equal to {b} and greater than {c}")
        elif a==b and a<c:
            print(f"{a} is equal to {b} and smaller than {c}")
        elif a>b and a==c:
            print(f"{a} is greater than {b} and equal to {c}")
        elif a<b and a==c:
            print(f"{a} is smaller than {b} and equal to {c}")
        elif a<b and a<c:
            print(f"{a} is Smaller than {b} and {c}")
        else:
            print("All are equal")
gs=GreatSmall()
while True:
    x=int(input("Enter Number 1 : "))
    y=int(input("Enter Number 2 : "))
    z=int(input("Enter Number 3 : "))
    gs.check(x,y,z)
