class Vehicle:
    name=""
    model=""
    price=0.0
    def details(self,n,m,p):
        self.name=n
        self.model=m
        self.price=p
    def show(self):
        print(f"Vehicle Name : {self.name}, Vehicle Model : {self.model}, Vehicle Price : {self.price}")

class Owner(Vehicle):
    name=""
    addr=""
    phone=0
    def o_details(self,n,a,p):
        self.name=n
        self.addr=a
        self.phone=p
    def show_det(self):
        print(f"Owner Name : {self.name}, Owner Address : {self.addr}, Owner Contact : {self.phone}")

own=Owner()
n=input("Enter Vehicle Name : ")
m=input("Enter Vehicle Model : ")
p=float(input("Enter Vehicle Price : "))
own.details(n,m,p)
own.show()

on=input("Enter Owner Name : ")
oa=input("Enter Owner Address : ")
op=int(input("Enter Owner Phone No. : "))
own.o_details(on,oa,op)
own.show_det()
