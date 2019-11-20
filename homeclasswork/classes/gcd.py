# This program uses recursion to find the GCD of two numbers


# if x can be evenly divded by y, then gcd(x, y) = y
# otherwise, gcd(x, y) = gcd(y, remainder of x/y)

def main():
    # get two numbers
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    # Display GCD
    print("The GCD of ")
    print("the two numbers is ", gcd(num1, num2))

# The gcd function returns the gcd of two numbers
def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)

main()