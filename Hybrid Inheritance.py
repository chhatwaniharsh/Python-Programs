class A:
    p=10
class B:
    q=20
class C(A,B):
    r=30
class D(C):
    s=40
class E(C):
    t=50
dobj=D()
print(dobj.p)
print(dobj.q)
print(dobj.r)
print(dobj.s)
print()
eobj=E()
print(eobj.p)
print(eobj.q)
print(eobj.r)
print(eobj.t)
