start=int(input("Enter Start : "))
stop=int(input("Enter Stop : "))
def check(st,sp):
    n=0
    for i in range(st,sp):
        if i%2==0:
            n+=1
            print(i)
    print("Total Even Number :",n)
check(start,stop)
