def sum(n):

    if n == 1: #base case
        return 1
    else:
        return n + sum(n-1) #recursive call
    
n = int(input("Enter a number: "))
print("Sum of numbers from 1 to", n, "is:", sum(n))

#Factorial of a number using recursion
def fact (n):
     if n == 0:
         return 1
     
     else:
         return n * fact(n - 1)
     
print("Factorial of 5 : ", fact(5))

