l=[1,2,3,6,4,20]
for i in range(len(l)-1):
    if l[i]<l[i+1]:
        continue
    else:
        print("your list is not sorted")
        break
else:
    print("your list is sorted")
