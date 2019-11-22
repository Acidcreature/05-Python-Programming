# 1: Recognize the following strings:
import re

#string = "bat bit but hat hit hut"

#pattern = re.compile(r'[a-zA-Z]{3}')
#matches = pattern.finditer(string)

#for match in matches:
#    print(match)

# 2: Match any pair of words separated by a single space,
# first and last names

#fl_list = """
#John Smith
#Kim Possible
#Bill Gates
#Goose
#Drake
#"""

#pattern = re.compile(r'\w+[ ]\w+')
#matches = pattern.findall(fl_list)

#for match in matches:
#    print(match)

# 3  First M. Last

names = """
Perry, Reuben
Pratt, Timothy
Last, Name
test
Test 
"""

#pattern = re.compile(r'\w+,\s+\w+')
#matches = pattern.finditer(names)

#for match in matches:
#    print(match)


# 4 identifiers

identifiers = '''
False
class
1test
test1
'''

pattern = re.compile(r'\b[a-zA-Z_][\w]+')
matches = pattern.finditer(identifiers)

for match in matches:
    print(match)