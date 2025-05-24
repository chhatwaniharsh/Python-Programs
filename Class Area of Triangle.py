class Triangle:
    def area(self,b,h):
        a=0.5*b*h
        print("Area :",a)
t1=Triangle()
base=int(input("Enter base of triangle : "))
height=int(input("Enter height of triangle : "))
t1.area(base,height)
