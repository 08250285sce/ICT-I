m1 = int(input("Enter the marks of subject 1: "))
m2 = int(input("Enter the marks of subject 2: "))
m3 = int(input("Enter the marks of subject 3: "))


def calculate_total(m1, m2, m3):
    total = m1 + m2 + m3
    print("The sum is:", total)
    return total

def calculate_average(m1, m2, m3):
    average = (m1 + m2 + m3) / 3
    print("The average of 3 marks is: %.2f" % average)
    return average

calculate_total(m1, m2, m3)
avg = calculate_average(m1, m2, m3)

if avg >= 50:
    print("Pass")
else:
    print("Fail")



def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


number = int(input("Enter a number: "))
print("The number is:", check_even_odd(number))