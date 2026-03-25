def factors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

num = int(input("Enter a number: "))

product = factors(num)

if product > 0:
    print(f"The number of factors of {num} is: {product}")
else:
    print(f"No factor of {num} is found")