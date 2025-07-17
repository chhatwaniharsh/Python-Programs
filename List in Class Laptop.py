class Laptop:
    def __init__(self,n,m,p):
        self.name=n
        self.model=m
        self.price=p
    def __str__(self):
        return f"Laptop Name : {self.name}, Laptop Model : {self.model}, Laptop Price : {self.price}"
    
l1=Laptop("Lenovo","LOQ",85200)
l2=Laptop("HP","Victus",73000)

laptop_list=[l1,l2]
for i in laptop_list:
    print(i)

