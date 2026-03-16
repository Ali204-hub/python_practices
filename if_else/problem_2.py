print("Enter your marks in the following subjects:")
a= int(input("enter your marks in maths:"))
b= int(input("enter your marks in biology:"))
c= int(input("enter your marks in chemistry:"))
total_percentage = (100*(a+b+c))/300
if(total_percentage>=40):
    print("Congratulations! you have passed the exam")
else:
    print("Sorry! try again next year")