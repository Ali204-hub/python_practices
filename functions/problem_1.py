def greatest(a,b,c):
    if a>b and a>c:
        print(a," is greatest")
    elif b>c and b>a:
        print( b," is greatest")
    else:
        print( c," is greatest")
a=100
b=44
c=55
print(f"the greatest number is {greatest(a,b,c)}")
