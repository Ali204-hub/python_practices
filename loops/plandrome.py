# your string will be plandrome in one way when its reversing order will be the same as the original name
a=input("enter any string which you want to check whether it's palindrome or not" )
b=""
for i in range( len(a)-1,-1,-1):
    b=b+a[i]
if b==a:
    print("YOUR string IS PLANDROME")
else:
    print("your string is not plandrome")

