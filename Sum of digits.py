num=int(input("Enter Number : "))
n1=num
s=0

while n1>0:
    d=n1%10
    s+=d
    n1=n1//10
    
print("Number :",num)
print("Sum of Digits :",s)
