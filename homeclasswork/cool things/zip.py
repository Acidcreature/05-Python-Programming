# Zip() Function
# The zip function is good for taking two different sequences
# of data and pair them together

# set up two lists
prices = [72.51, 9.27, 153.74, 30.23, 53.00]
names = ['CAT', 'GE', 'MSFT', 'AA', 'IBM']

# use for loop and zip to pair the lists together
for name, price in zip(names, prices):
    print(name, '=', price)

