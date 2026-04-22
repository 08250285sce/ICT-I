def sum() :
    a = 5
    b = 10
    print("The Sum of a and b is:", a + b)
     
def product() :
    a = 5
    b  = 10
    print("The product of a and b is:", a * b)

sum ()
product()

#Parameters
def sum_with_parameters(a,b):
    print("The sum of", a, "and", b, "is:", a + b)

sum_with_parameters(3, 7) #argument= function call


def product_with_parameters(a,b):
    print("The product of", a, "times", b, "is:", a * b)

product_with_parameters(3, 7)

#Return value
def sum_with_return(a, b):
    return a + b
print("The sum of 4 and 6 is:", sum_with_return(4, 6))
print(sum_with_return(4, 6))

def product_with_return(a, b):
    return a * b
print("The product of 4 times 6 is:", product_with_return(4, 6))
print(product_with_return(4, 6))

