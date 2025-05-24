class Whole:
    def showSum(self,n):
        c=0
        for i in range(0,n+1):
           c+=i
        print("Total Count :",c)
w1=Whole()
n=int(input("Enter ending number : "))
w1.showSum(n)
