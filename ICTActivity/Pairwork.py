Name = input("Enter your name")
Subject1= float(input("Enter the marks of first subject:"))
Subject2 = float(input("Enter the marks of second subject:"))
Subject3 = float(input("Enter the marks of third subject:"))
Subject4 = float(input("Enter the marks of fourth subject:"))
average = (Subject1 + Subject2 + Subject3+ Subject4)/ 4
print("The average is ""%.2f" %average)

attendance = float(input("Enter attendance (%): "))
if (average >= 90 and Subject1 >= 40 and Subject2 >= 40 and Subject3 >= 40 and Subject4 >= 40 and attendance >= 80):
    print("Grade: A+")
    result = print("Passed")
    print("You are Eligible for Reward")
elif (average >= 80 and Subject1 >= 40 and Subject2 >= 40 and Subject3 >= 40 and Subject4 >= 40 and attendance >= 80):
    print("Grade: A")
    result = print("Passed")
    print("You are Eligible for Reward")
elif (average >= 70 and Subject1 >= 40 and Subject2 >= 40 and Subject3 >= 40 and Subject4 >= 40 and attendance >= 80):
    print("Grade: B")
    result = print("Passed")
    print("You are Eligible for Reward")
elif (average >= 60 and Subject1 >= 40 and Subject2 >= 40 and Subject3 >= 40 and Subject4 >= 40 and attendance >= 80):
    print("Grade: C")
    result = print("Passed")
    print("You are not Eligible for Reward")
elif (average >= 50 and Subject1 >= 40 and Subject2 >= 40 and Subject3 >= 40 and Subject4 >= 40 and attendance >= 80):
    print("Grade: D")
    result = print("Passed")
    print("You are not Eligible for Reward")
elif (average >= 40 and Subject1 >= 40 and Subject2 >= 40 and Subject3 >= 40 and Subject4 >= 40 and attendance >= 80):
    print("Grade: E")
    result = print("Passed")
    print("You are not Eligible for Reward")
else:
    print("Grade: F")
    result = print("Failed")
    print("You are not Eligible for Reward")

print("Your final results is:")
print(f"Student Name: {Name}")
print(f"Attendance: {attendance}%")
print(f"Your Average is: {average}%")
print(f"Your Result is: {result}%")

print(f"There are 12 girls and 16 boys in our class. So in total we have {12 + 16} students")
