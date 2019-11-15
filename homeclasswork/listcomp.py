# List Comprehension
# Good way to create a new list by performing an
# operation on each item in an existing list

# Seperating string into letters
#chars = []
#for ch in 'Daniel':
#    chars.append(ch)
#print(chars)

#chars2 = [ch for ch in 'Daniel']
#print(chars2)

# Get the square of each x in my range of 0-10
#squares = [x*x for x in range(11)]
#print(squares)

# list of tuples
#list1 = [1, 2, 3]
#list2 = ['a', 'b', 'c']
#combined_lists = [(x, y) for x in list1 for y in list2]
#print(combined_lists)

# list comprehension with optional predicate
#evens = [x for x in range(21) if x % 2 == 0]
#print(evens)

# list comprehension with optional predicate
#numbers = [x for x in range(21) if x % 2 == 0 if x % 5 == 0]
#print(numbers)

# if else list comprehension
#obj = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]
#print(obj)

# Flatten a list
#matrix = [[1, 2, 3], [4, 5, 6,], [7, 8, 9]]
#flat_list = [num for row in matrix for num in row]
#print(flat_list)

#nums = [1, 2, 3, 4]
#str = ['a', 'b', 'c', 'd']
# i want a (Letter, number) pair for each letter in
# str and each number in nums

#my_list = []
#for letter in str:
#    for num in nums:
#        my_list.append((letter, num))
#print(my_list)

#my_list2 = [(letter, num) for letter in str for num in nums]
#print(my_list2)

# set comprehension
#nums = [1, 1, 2, 1, 3, 9, 4, 5, 5, 6, 7, 7, 8, 9, 10]
#my_set = set()
#for n in nums:
#    my_set.add(n)
#print(my_set)
#
#my_set2 = {n for n in nums}
#print(my_set2)

# Dictionary comprehension
#names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
#secrets = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# I want a dict{'Name' : 'Secret'} for each name, secret
# in zip(names, secrets)

#my_dict = {}
#for name, secret in zip(names, secrets):
#    my_dict[name] = secret
#print(my_dict)

#my_dict2 = {name:secret for name, secret in zip(names, secrets)}
#print(my_dict2)

# Generator Expression
# I want to yield 'n*n' for each 'n' in nums
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def gen_func(nums):
    for n in nums:
        yield n*n
my_gen = gen_func(nums)

print(next(my_gen))
print(next(my_gen))

my_gen2 = (n*n for n in nums)
for i in my_gen2:
    print(i)






