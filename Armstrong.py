n=int(input("Enter Number : "))
g=str(n)
l=len(g)
count=0
for i in g:
    d=int(i)
    e=d**l
    count+=e
if count==n:
    print("Yes")
else:
    print("No")
