num=int(input("Enter Number : "))
n1=num
rev=0

while n1>0:
    d=n1%10
    rev=rev*10+d
    n1=n1//10
    
print("Original Number :",num)
print("Reversed Number :",rev)
