def add(*args):
    s=0
    for i in args:
        s+=i
    print(s)
add()
add(10,20,30,40,50)


def sub(a,b):
    c=a-b
    print(c)

sub(b=10,a=20)
