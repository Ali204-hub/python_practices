# # the reverse of number on new line
# a=int(input("Enter any number:"))
# while a>0:
#     print(a%10)
#     a= a//10

# # the reverse of number on the same line
# b=int(input("Enter the number: "))
# rev=0
# while b>0:
#     rev=rev*10+b%10
#     b=b//10
# print( rev)

#  checking of palindromic number

b=int(input("Enter the number: "))
copy =b
rev=0
while b>0:
    rev=rev*10+b%10
    b=b//10
if copy==rev:
    print("your number is palindromic")
else:
    print("your number is not palindromic")
