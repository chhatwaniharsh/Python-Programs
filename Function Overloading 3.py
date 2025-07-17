from multipledispatch import dispatch

@dispatch(bool,bool)
def check(a,b):
    ans=a and b
    return ans

@dispatch(bool,bool,bool)
def check(a,b,c):
    ans=(a and b) or c
    return ans

ans=check(True,False)
print(ans)
ans=check(True,False,True)
print(ans)
