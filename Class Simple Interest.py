class SimpleInt:
    def check(self,p,r,t):
        SI=(p*r*t)/100
        print("Simple Interest :",SI)
s1=SimpleInt()
P=int(input("Enter Principle Amount : "))
R=int(input("Enter Rate of Interest : "))
T=int(input("Enter Time in years : "))
s1.check(P,R,T)
