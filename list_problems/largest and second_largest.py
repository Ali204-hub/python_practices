l=[23,32,33,56,326,99,100]
largest=l[0]
sec_largest =l[0]
for i in l:
    if i>largest:
        sec_largest=largest
        largest=i
    else:
        if i>sec_largest:
            sec_largest=i
print(largest,sec_largest)