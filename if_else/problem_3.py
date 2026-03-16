spam_phrases = ["MAKE A LOT OF MONEY", "BUY NOW", "CLICK HERE", "SUBSCRIBE NOW"]
message = input("Enter your message: ").upper()
if any(phrase in message for phrase in spam_phrases):
    print("This is spam message. Beware!")
else:
    print("This is not a spam message.")