def sum(n):
    if n==1:
        return 1
    d= sum(n-1)+n
    return d
n=int(input("Enter the number:"))
c=sum(n)
print(c)