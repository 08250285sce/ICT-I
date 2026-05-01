n = int(input("Enter a number: "))
num =lambda x: "Positive" if x > 0 else ("Negative" if x < 0 else "Zero")
print(num(n))