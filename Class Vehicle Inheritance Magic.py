class Vehicle:
    def assign(self,n,m,p):
        self.name=n
        self.model=m
        self.price=p
    def show(self):
        print(f"Vehicle Name : {self.name}, Vehicle Model : {self.model}, Vehicle Price : {self.price}")

class Owner(Vehicle):
    def __init__(self,n,a,c):
        self.name=n
        self.address=a
        self.contact=c
    def __str__(self):
        return f"Owner Name : {self.name}, Owner Address : {self.address}, Owner Contact : {self.contact}"

oobj=Owner("ABC","xyz",8798562520)
oobj.assign("Mahindra","XUV",1700000)
oobj.show()
print(oobj)
