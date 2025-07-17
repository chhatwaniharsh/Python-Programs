from multipledispatch import dispatch

@dispatch(int,int)
def add(a,b):
    ans=a+b
    print(ans)

@dispatch(str,str)
def add(a,b):
    ans=a+b
    print(ans)

add("Harsh"," Chhatwani")
add(10,20)
