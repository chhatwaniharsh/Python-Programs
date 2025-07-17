try:
    print("try block starts")
    fn=int(input("Enter First Number : "))
    sn=int(input("Enter Second Number : "))
    ans=fn/sn
    print(ans)
    print("try block starts")
except ZeroDivisionError as zde:
    print(zde)
    print("except-block1 There is some exception in try block.")
    print("Please choose a non-zero value as deno.")
except ValueError as ve:
    print(ve)
    print("except-block2 There is some exception in try block.")
    print("Please enter a numeric whole numbers only")
except Exception as e:
    print(e)
    print("except-block3 There is some exception in try block.")
else:
    print("else-block There is NO exception in try block.")
print("remaining code....")
print("last line.")
