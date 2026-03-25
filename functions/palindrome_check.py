def is_palindrome(n):
    return str(n) == str(n)

def main():
    num = int(input("Enter number: "))
    if is_palindrome(num):
        print("Palindrome")
    else:
        print("Not Palindrome")

main()