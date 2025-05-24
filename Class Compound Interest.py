class CompoundInt:
    def check(self,p,r,t):
        A=P*(1+(R/100))**T
        CI = A-P
        print("Compound Interest :",CI)
c1=CompoundInt()
P=int(input("Enter Principle Amount : "))
R=int(input("Enter Rate of Interest : "))
T=int(input("Enter Time in years : "))
c1.check(P,R,T)
