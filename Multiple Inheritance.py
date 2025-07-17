class A:
    p=10
class B:
    q=20
class C(A,B):
    r=30
cobj=C()
print(cobj.p)
print(cobj.q)
print(cobj.r)
