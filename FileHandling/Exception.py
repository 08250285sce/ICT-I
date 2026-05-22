try: 
    n = float(input("Enter a number: "))
    res = 100 / n
except ZeroDivisionError: 
    print("You can't divide by zero!")

except ValueError: 
    print("Enter a valid number!")

except:
    print("An unexpected error occurred")

else:
    print("Result is", res)

finally:
    print("Execution complete.")
    