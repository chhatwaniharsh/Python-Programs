class Armstrong:
    def check(self,n):
        a=n
        s=0
        while(a>0):
             rem=a%10
             c=rem**3
             s+=c
             a=a//10
        if s==n:
            print("Armstrong Number")
        else:
            print("Not Armstrong Number")
num=int(input("Enter Number : "))
a1=Armstrong()
a1.check(num)
