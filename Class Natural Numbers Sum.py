class Natural:
    def showSum(self,n):
        c=0
        for i in range(1,n+1):
           c+=i
        print("Total Count :",c)
n1=Natural()
n=int(input("Enter ending number : "))
n1.showSum(n)
