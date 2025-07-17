try:
    fn=int(input("Enter first number : "))
    sn=int(input("Enter second number : "))
    ans=fn/sn
    print(ans)
except ZeroDivisionError:
    print("Please enter non-zero value as denominator.")
else:
    print("Division Successfull")
