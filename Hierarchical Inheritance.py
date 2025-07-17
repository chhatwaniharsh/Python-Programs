class A:
    p=10
class B(A):
    q=20
class C(A):
    r=30
bobj=B()
print(bobj.p)
print(bobj.q)
print()
cobj=C()
print(cobj.p)
print(cobj.r)
