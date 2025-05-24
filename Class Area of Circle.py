class Circle:
    def area(self,r):
        ar=3.14*r*r
        print("Area of Circle :",ar)
c1=Circle()
rad=int(input("Enter radius of circle : "))
c1.area(rad)
