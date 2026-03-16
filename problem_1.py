a=int(input("enter a number: "))
b=int(input("enter a number: "))
c=int(input("enter a number: "))
d=int(input("enter a number: "))
if a>=b and a>=c and a>=d:
    print("a is the largest number", a)
elif b>=a and b>=c and b>=d:
    print("b is the largest number", b)
elif c>=a and c>=b and c>=d:
    print("c is the largest number", c)
else:
    print("d is the largest number", d)
