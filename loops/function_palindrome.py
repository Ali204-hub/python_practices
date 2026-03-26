def pallindrome(st):
        b=""
        for i in range( len(st)-1,-1,-1):
            b=b+st[i]
        if b==st:
         print(f"{st} string IS PLANDROME")
        else:
         print(f"{st} string is not plandrome")

pallindrome("naman")
pallindrome("keek")
pallindrome("lol")
pallindrome("course")
