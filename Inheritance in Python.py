print("--Single Inheritance--")
class A:
    a=10
class B(A):
    b=20
bobj=B()
print(bobj.a)
print(bobj.b)

print("\n--Multiple Inheritance--")
class A:
    a=10
class B:
    b=20
class C(A,B):
    c=30
cobj=C()
print(cobj.a)
print(cobj.b)
print(cobj.c)

print("\n--Multilevel Inheritance--")
class A:
    a=10
class B(A):
    b=20
class C(B):
    c=30
class D(C):
    d=40
dobj=D()
print(dobj.a)
print(dobj.b)
print(dobj.c)
print(dobj.d)

print("\n--Hierarchical Inheritance--")
class A:
    a=10
class B(A):
    b=20
class C(A):
    c=30
bobj=B()
cobj=C()
print(bobj.a)
print(bobj.b)
print(cobj.a)
print(cobj.c)

print("\n--Hybrid Inheritance--")
class A:
    a=10
class B(A):
    b=20
class C(A):
    c=30
class D(B,C):
    d=40
dobj=D()
print(dobj.a)
print(dobj.b)
print(dobj.c)
print(dobj.d)
    
