import random
num=random.randint(1,100)
tries=0
while True:
    guess=int(input("guess a number"))
    if num==guess:
        tries+=1
        print(f" you are right you guessed the number is {tries}")
        break
    elif num<=guess:
        print("go a little lower")
        tries+=1
    elif num>=guess:
        print("go a little higher")
        tries+=1
    else:
        print("Sorry you are wrong")
        tries+=1

    
    
