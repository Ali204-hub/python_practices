p1="MAKE A LOT OF MONEY"
P2="BUY NOW"
P3="CLIICK HERE"
P4="SUBSCRIBE NOW"
message=input("Enter your message:")
if(p1 in message or P2 in message or P3 in message or P4 in message):
    print("this is spam message beware!")
else:
    print("this is not a spam message")