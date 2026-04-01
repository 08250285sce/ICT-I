age = int(input("Enter your age:"))
if age >= 18:
    registered_voter = input("Are you a registered voter? (True?False): ")
    registered_voter = registered_voter.lower() #convert input to boolean
    if registered_voter == "true":
        print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")