a=180
b=170
c=122
if a==b and b==c:
    print("all number are same")
elif a>b and b>c:
    print(f"{a} is greater than {b} and {c}")
elif b>c:
    print(f"{b} is greater than {a} and {c}")
else:
    print(f"{c} is greater than {b} and {a}")
