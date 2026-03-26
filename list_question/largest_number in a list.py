li=[13,33,55,6666,43,44,74]
largest=li[0]
index=0
for i in range(len(li)):
    if li[i] >largest:
        largest=li[i]
        index=i
print(f"your largest number is {largest}at {index}")