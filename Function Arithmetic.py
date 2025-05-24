'''
def add():
    a=10
    b=20
    c=a+b
    return c
def sub():
    a=10
    b=20
    c=a-b
    return c
def mul():
    a=10
    b=20
    c=a*b
    return c
def div():
    a=10
    b=20
    c=a/b
    return c

d=add()
print("Add :",d)
print("Sub :",sub())
print("Mul :",mul())
print("Div :",div())
'''

def arith():
    a=10
    b=20
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return add,sub,mul,div

print(arith())

a,s,m,d=arith()
print("Add :",a)
print("Sub :",s)
print("Mul :",m)
print("Div :",d)

a=arith()
for i in a:
    print(i)

