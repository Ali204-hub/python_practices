a="aliimam12934#$%%^^&"
char=0
spchar=0
digit=0

for i in a:
    if i.isdigit():
        digit+=1
    elif i.isalpha():
        char+=1
    else:
        spchar+=1
print(f"digits are{digit},Character are{char} and Special characters are{spchar}")
        