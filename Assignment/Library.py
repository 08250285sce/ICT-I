#input from the user
name = print(input("Enter your name :"))
books_borrowed = int(input("Enter number of days the book was borrowed : "))
days_late = int(input("Enter number of days late (0 if on time) :"))

#Fine Calculations
fine = 0
if (days_late ==0 ):
    print("no need for fine")
elif (days_late >=1 and days_late <=5):
    print("nu. 5 per day")
elif (days_late >=6 and days_late <=9):
    print("nu.10 per day")
else:
    print("nu.20 per day")
if (books_borrowed >30):
    print("WARNING! libary privilege may be restricted")
else:
    print("")