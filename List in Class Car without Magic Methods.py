class Car:
    def assign(self,n,m,no,c,p):
        self.name=n
        self.model=m
        self.number=no
        self.color=c
        self.price=p
    def disp(self):
        print(f"Car Name = {self.name}")
        print(f"Car Model = {self.model}")
        print(f"Car Number = {self.number}")
        print(f"Car Color = {self.color}")
        print(f"Car Price = {self.price}")

print("Without use of list")
c1=Car()
c1.assign("Mahindra",2012,"MH19BA2025","Red",1800000)
c1.disp()

print()

c2=Car()
c2.assign("XUV",2018,"MH19AA2486","Black",2700000)
c2.disp()

print()
print("Using List")

car_list=[c1,c2]
for i in car_list:
    print(i.disp())
