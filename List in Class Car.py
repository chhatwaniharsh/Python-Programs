class Car:
    def __init__(self,n,m,no,c,p):
        self.name=n
        self.model=m
        self.number=no
        self.color=c
        self.price=p
    def __str__(self):
        return f"Car Name={self.name}, Car Model={self.model}, Car number={self.number}, Car Color={self.color}, Car Price={self.price}"
c1=Car("Mahindra",2012,"MH19BA2025","Red",1800000)
c2=Car("XUV",2018,"MH19AA2486","Black",2700000)
car_list=[c1,c2]
for cars in car_list:
    print(cars)
