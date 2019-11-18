# enumerate()
# Enumerate iterates over different types of iterable objects
# and returns both the index and also the valu of each item.

# enumerate over some names
#names = ['Daniel', 'Joe', 'Jim', 'Travis']
#print(list(enumerate(names, start=6)))
#for item in enumerate(names):
#    print(item)

#for count, item in enumerate(names, 100):
#    print(f'Count: {count}, Item: {item}')

#my_string = 'Enumerating is Powerful'
#for idx, ch in enumerate(my_string):
#    print(f'Index is {idx} and character is {ch}')

# dictionary comprehension with enumerate()
names = ['Daniel', 'Joe', 'Jim', 'Travis']
my_dict = {k: v for k, v in enumerate(names)}
print(my_dict)
