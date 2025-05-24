num=int(input("Enter Number : "))
count=0
for i in range(1,num):
    if num%i==0:
        count+=i
if num==count:
    print("Perfect Number")
else:
    print("Not a perfect number")
