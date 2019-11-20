# reduce()
# Receives twp arguments, functions and iterable
# returns a single value
# good for rolling computation to sequential pairs of value
# in a list

# reduce come from functools module
import functools

# define our function
#def mult(x, y):
#    print("x = ", x, "y = ", y)
#    return x*y

# apply reduce to our function
#fact = functools.reduce(mult, range(1, 4))
#print('Factorial of 3 is ', fact)

# normal for loop
#product = 1
list = [1, 2, 3, 4]
#for num in list:
#    product = product * num
#print(product)

# using reduce
from functools import reduce
product = reduce((lambda x, y: x*y), list)
print(product)