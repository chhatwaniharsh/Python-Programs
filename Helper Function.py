def prime(g):    
    if g<=1:
        return False
    for i in range(2,g):
        if g%i==0:
            return False
    return True

num=int(input("Enter a number : "))
if prime(num):
    print("Prime Number")
else:
    print("Not Prime Number")





'''
while True :
    num=int(input("Enter a number : "))
    a=prime(num)
    print(a)
'''

