#Create a python module helperfunctions.py with the following functions.
#add - returns the sum of two numbers
#diff - returns the difference between two numbers
#product - returns the product of two numbers
#greatest - returns the greatest of two numbers.

def helperfunctions(a, b):
    add = a + b
    diff = abs(a - b)
    product = a * b
    greatest = max(a, b)

    return add, diff, product, greatest

