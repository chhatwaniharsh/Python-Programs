try:
    fn=int(input("Enter first number : "))
    sn=int(input("Enter second number : "))
    ans=fn/sn
    print(ans)
except ValueError:
    print("Please enter a numeric whole value only.")
