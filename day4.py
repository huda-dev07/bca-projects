year = int(input("enter year:"))

if (year % 400 ==0) or (year % 4 == 0 and year % 100 !=0):
    print("leap year")
else:
    print("not leap year")
a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))

if a>=b and a>=c:
    print(a)
elif b>=a and b>=c:
    print(b)
else:
    print(c)