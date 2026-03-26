n=int(input("enter the number you want get sum of all odd and even numbers in the given number:"))
even =0
odd =0
for i in range( 1,n+1):
    if i%2==0:
        even +=i
    else:
        odd+=i
print(f"the sum of odd and even number is : {even} and {odd}")
