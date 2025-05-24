class Armstrong:
    def check(self,a):
        count=0
        b=str(a)
        for i in b:
            c=int(i)
            count+=c*c*c
        if count==a:
            print("Armstrong Number")
        else:
            print("Not Armstrong Number")
a1=Armstrong()
num=int(input("Enter Your number : "))
a1.check(num)
