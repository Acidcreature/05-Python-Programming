# Dictionaries
# A dictionary is an object that stores a collection of data. Each element in a dictionary
# has two parts, a key and a value. You use a key to locate a specific value.

# Creating a dictionary

#phonebook = {'Chris':'555-1111','Katie':'555-2222','Joanne':'555-3333'}
#print(phonebook)
#
##get a specific value
"""
print(phonebook['Katie'])

##Using the in and not in operators
if 'Chris' in phonebook:
    print(phonebook['Chris'])

if 'David' not in phonebook:
    print("Not in phonebook")

##adding an element
phonebook['David'] = '555-4444'
print(phonebook)

#remove an element
del phonebook['David']
print(phonebook)

#Find length
length_dict = len(phonebook)
print(length_dict)

#Using update to add items to the dictionary
print(phonebook)
phonebook.update({'David':'555-444', 'Chris':'555-1234'})
print(phonebook)

phonebook2 = {'Jim':'123-4567'}
phonebook.update(phonebook2)
print(phonebook)

test_scores = {
    'Kayla':[88,92,100],
    'Luis':[95,74,81],
    'Sophie':[72,88,91],
    'Ethan':[78,75,78]}
print(test_scores)
#Accessing values of diff types
kayla_scores = test_scores['Kayla']
print(kayla_scores[1])

#initialize an empty dictionary
empty_dict = {}
print(empty_dict)
empty_dict[1] = 'This is a value'
print(empty_dict)

#Interating over a dictionary
for key in phonebook:
    print(key)
for key in phonebook:
    print(key, phonebook[key])

#The clear method
dictionary.clear()
phonebook.clear()
print(phonebook)

# the get method
dictionary.get(key, default)

value = phonebook.get('Katie', 'Entry not found')
print(value)
value2 = phonebook.get('David', 'Entry not found')
print(value2)

# The items method
print(phonebook.items())

#for key, value in phonebook.items():
    print(key, value)

# The keys method
for key in phonebook.keys():
    print(key)
# The values method
for value in phonebook.values():
    print(value)

# The pop method (removes and returns key-value pair)
 dictionary.pop(key, default)
phone_num = phonebook.pop('Chris', 'Entry not found')
print(phone_num)
print(phonebook)
phone_num2 = phonebook.pop('Andy', 'Entry not found')
print(phone_num2)
print(phonebook)

#the popitem method
key, value = phonebook.popitem()
print(key, value)
"""
# Multi Dimensional Dictionary
​
# Intitialize instrument dictionary
instruments = {'drums': {'color':'black', 'sound':'boom'},
               'guitar': {'color':'blue', 'sound':'wahhh'}}
print('Original', instruments)
​
# Add something to the nested dictionary
instruments.update({'violin':{'color':'brown', 'sound':'whineeee'}})
print('After updating', instruments)
​
# More ways to add instruments
instruments['bass'] = {'color':'purple', 'sound':'slappadabass'}
print('After adding bass', instruments)
​
# Access items/nested items within our dictionary
print('guitar', instruments['guitar'])
print('guitar sound', instruments['guitar']['sound'])
​
# Iterate through nested dictionary
for instrument, properties in instruments.items():
    print('Instrument: ', instrument)
    for property in properties:
        print(property + ":", properties[property])
