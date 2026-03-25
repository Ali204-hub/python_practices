def is_leap(year):
     if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
          print("this is leap year")
     else:
          print("not a leap year")

year=int(input("Enter the year:"))
is_leap(year)