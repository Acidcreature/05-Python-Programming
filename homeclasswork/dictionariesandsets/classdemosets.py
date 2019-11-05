# Sets
# A Collection of unique values and works like a mathematical set

# All the elements in a set must be unique, no two elements have the same value.

# Sets are unordered, which means that the elements are not stored in any particular order.

# The elements that are stored in a set can be of different data types

# Creating a set
#my_set = set(['a', 'b', 'c'])
#print(my_set)

#my_set2 = set('abc')
#print(my_set2)

#my_set3 = set('aabbcc')
#print(my_set3)

#my_set4 = set('one two three')
#print(my_set4)

# Find the length of a set
#print(len(my_set4))

# Adding an removing elements of a set
#new_set = set()
#new_set.add(1)
#new_set.add(2)
#new_set.add(3)
#print(new_set)

#new_set.update([4, 5, 6])
#print('after update', new_set)

#new_set2 = ([7, 8, 9])
#new_set.update(new_set2)
#print('After variable update', new_set)

#new_set.remove(1)
#print(new_set)
# keyerror
# new_set.remove(10)

#using discard
#new_set.discard(10)
#print(new_set)

# using for loop to iterate over a set

new_set3 = set(['a', 'b', 'c'])
for val in new_set3:
    print(val)

# using in and not in operators to test a value in a set
numbers_set = ([1, 2, 3])
if 1 in numbers_set:
    print('The value 1 is in the set')

if 90 not in numbers_set:
    print('The value 90 is not in the set')

# find the union of sets
set1 = set([1, 2, 3, 4])
set2 = set([3, 4, 5, 6])
set3 = set1.union(set2)
print('set3', set3)
set5 = set1 | set2
print('set5', set5)

# Find the intersection of sets
set4 = set1.intersection(set2)
print('set4', set4)

# find the difference of sets (Whats in SET() that isnt in .difference(SET))
set7 = set1.difference(set2)
print('set7', set7)

# find the symmetric difference of sets
set8 = set1.symmetric_difference(set2)
print('set8', set8)

# Finding subsets and supersets
set9 = set([1, 2, 3, 4])
set10 = set([1, 2])
print(set10.issubset(set9))
print(set9.issuperset(set10))