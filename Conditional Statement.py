'''

#Number is Positive or Negative
num=int(input("Enter the number : "))
if num==0:
    print("Number is Zero")
elif num>0:
    print(num,"is Positive")
else:
    print(num,"is Negative")


#Number is divisible by 5 or not
num=int(input("Enter the number : "))
if num%5==0:
    print(num,"is Divisible by 5")
else:
    print(num,"is Not Divisible by 5")


#Even or Odd
num=int(input("Enter the number : "))
if num%2==0:
    print(num,"is even")
else:
    print(num,"is odd")


#Eligible for votting or not
age=int(input("Enter Age : "))
if age>=18:
    print("Congratulations, You are ELIGIBLE for voting")
else:
    print("Sorry, You are NOT ELIGIBLE for voting")


#Leap Year or Not
year=int(input("Enter your Year : "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Leap Year")
        else:
            print("Not leap year")
    else:
        print("Leap Year")
else:
    print("Not leap year")


#Check the grade as per marks of student
marks=int(input("Enter your percentage : "))
if marks>100 or marks <0:
    print("Please enter Valid Marks")
elif marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=60:
    print("Grade C")
elif marks>=40:
    print("Pass")
else:
    print("Fail")


#Greater number between two number
a=int(input("Enter A : "))
b=int(input("Enter B : "))
if a>b:
    print("A is greater than B")
elif a<b:
    print("A is smaller than B")
else:
    print("A is equal to B")


#heck the grade as per average of 5 marks of student
a=int(input("Enter Marks of subject 1 : "))
b=int(input("Enter Marks of subject 2 : "))
c=int(input("Enter Marks of subject 3 : "))
d=int(input("Enter Marks of subject 4 : "))
e=int(input("Enter Marks of subject 5 : "))
f=a+b+c+d+e
print(f)
marks=(a+b+c+d+e)/5
print(marks)
if marks>100 or marks <0:
    print("Please enter Valid Marks")
elif marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=60:
    print("Grade C")
elif marks>=40:
    print("Pass")
else:
    print("Fail")


#Greater number in three number
a=int(input("Enter A : "))
b=int(input("Enter B : "))
c=int(input("Enter C : "))

if a>b:
    if a>c:
        print("A is Greater than B and C")
    elif a==c:
        print("A is Greater than B and Equals to C")
    else:
        print("A is Greater than B but Smaller than C")
elif a==b:
    if a>c:
        print("A is Equals to B and Greater than C")
    elif a==c:
        print("A is Equals to B and C")
    else:
        print("A is Equals to B but Smaller than C")
else:
    if a>c:
        print("A is Smaller than B but Greater than C")
    elif a==c:
        print("A is Smaller than B and Equals to C")
    else:
        print("A is Smaller than B and C")


#Check the quadrant based on x and y axis given by user
x=int(input("Enter X-axis Point : "))
y=int(input("Enter Y-axis Point : "))

if x==0 and y==0:
    print("At Origin")
elif x>0 and y>0:
    print("1st Quadrant")
elif x<0 and y>=0:
    print("2nd Quadrant")
elif x<0 and y<0:
    print("3rd Quadrant")
elif x>=0 and y<0:
    print("4th Quadrant")


#Check the type of triangle based on angle entered by user
a=float(input("Enter 1st angle of triangle : "))
b=float(input("Enter 2nd angle of triangle : "))
c=float(input("Enter 3rd angle of triangle : "))
d=a+b+c
if d==180:
    print("Triangle is Valid")
    
    if a==b and a==c:
        print("Triangle is Equilateral")
    elif a==b or a==c or b==c:
        print("Triangle is Isoscale")
    else:
        print("Other type of triangle")
        
else:
    print("Triangle is invalid")


#Electricity bill of units entered by user
unit=int(input("Enter number of units : "))
if unit<100 and unit>=0:
    print("0")
elif unit>=300:
    total=unit*20
    print(total)
elif unit>=200:
    total=unit*10
    print(total)
else:
    total=unit*5
    print(total)


#Electricity bill of units and rate entered by user
unit=int(input("Enter number of units : "))
if unit<100 and unit>=0:
    print("0")
else:
    rate=int(input("Enter rate per unit : "))
    total=unit*rate
    print(total)


#Get the total cost for 1st month, per month, and year by taking rent and deposit from user
rent=int(input("Enter rent : "))
depo=int(input("Enter Deposit : "))

unit=int(input("Enter number of units : "))
if unit<100 and unit>=0:
    total=rent+depo
    print("Cost for 1st Month:",total)
    print("Cost per Month :",rent)
    print("Cost for year :",rent*12)
else:
    rate=int(input("Enter rate per unit : "))
    total_bill=unit*rate
    print("Electricity Bill :",total_bill)
    total=rent+depo+total_bill
    print("Cost for 1st Month:",total)
    print("Cost per Month :",rent+total_bill)
    print("Cost for year :",(rent+total_bill)*12)
'''

