try:
    print("try block starts")
    fn=10
    sn=0
    ans=fn/sn
    print(ans)
    print("try block ends")
except ZeroDivisionError:
    print("except-block There is some exception in try block.")
    print("Please choose a non-zero value as deno.")
else:
    print("else-block There is NO exception in try block.")
print("remaining code....")
print("last line.")
