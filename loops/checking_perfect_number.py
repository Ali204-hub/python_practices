n=int(input("enter number you want to check whether it's perfect or not:"))
# the number will be perfect in this way  when the sum of its factor will equal to the  number otherwise the number will be not perfect. lets check it!
sum =0
for i in range(1,n):
    if n%i==0:
        sum=sum+i 
if sum==n:
    print( f"the number{n}is perfect")
else:
    print( "the number is not perfect")
     
    