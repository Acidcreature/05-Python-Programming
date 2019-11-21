# Regular Expressions or Regex

import re

#text_to_match ='''Daniel 1234 abcd'''

#print('\tTab')
#print(r'\tTab')

# compile() will allow us to seperate our patten matches into a variable
# that makes it easier to reuse our variable
#pattern = re.compile(r'Daniel')
#match = pattern.match(text_to_match)
#print(match)


# match()
# Determines if the regex matches at the beginning of the string
# returns None if its not at the beginning, same as ^ anchor
#match = pattern.match(text_to_match)
#print(match)


# search()
# lets us search entire string
#pattern = re.compile(r'1234')
#searched_item = pattern.search(text_to_match)
#print(searched_item)

# finditer()

#text_to_match ='''Daniel 1234 abcd
#this.thing@email.com'''

#pattern = re.compile(r'abcd')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)



# Meta characters

# . Any character except the new line '\n'
#pattern = re.compile(r'.')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)

# literal .
#pattern = re.compile(r'\.')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)

# \d - finds any digit from 0-9
#pattern = re.compile(r'\d')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)

# \D Finds non digit from 0-9
#pattern = re.compile(r'\D')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)

#text_to_match ='''Daniel    1234 abcd
#this.thing@email.com
#this_other-thing@email.com'''

# \w finds any Word characters (a-z, A-Z, 0-9, _)
#pattern = re.compile(r'\w')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)

# \W finds any Non-Word characters
#pattern = re.compile(r'\W')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)

# \s Finds any Whitespace (space, tabs, new lines)
#pattern = re.compile(r'\s')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)

# \S Finds Non-Whitespace
#pattern = re.compile(r'\S')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)


# ******* Anchors *******
# Anchors don't match chars, match invisible positions before or after chars

#text_to_match = """lol lololol
#Daniel 1234 abcd
#this.thing@email.com
#    this_other-thing@email.com"""

# \b finds word boundaries, 
# anything prefixed with a start of a new line, start of a string, spaces, tabs
#pattern = re.compile(r'\blol')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)

# \B finds non-word boundaries
#pattern = re.compile(r'\Blol')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)

# ^ - finds matches at beginning of string
#pattern = re.compile(r'^lol')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)

# $ finds matches at end of string
#pattern = re.compile(r'com$')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)


#text_to_match = """lol lololol
#Daniel 1234 abcd
#this.thing@email.com
#    this_other-thing@email.com
#210-444-4444
#512*888*8888
#"""


#pattern = re.compile(r'\d\d\d')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)

# Regular Expressions or Regex

#import re

#text_to_match ='''Daniel 1234 abcd'''

#print('\tTab')
#print(r'\tTab')

# compile() will allow us to seperate our patten matches into a variable
# that makes it easier to reuse our variable
#pattern = re.compile(r'Daniel')
#match = pattern.match(text_to_match)
#print(match)


# match()
# Determines if the regex matches at the beginning of the string
# returns None if its not at the beginning, same as ^ anchor
#match = pattern.match(text_to_match)
#print(match)


# search()
# lets us search entire string
#pattern = re.compile(r'1234')
#searched_item = pattern.search(text_to_match)
#print(searched_item)

# finditer()
# takes all matches and uses them to iterate

#text_to_match ='''Daniel 1234 abcd
#this.thing@email.com'''

#pattern = re.compile(r'abcd')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)



# Meta characters

# . Any character except the new line '\n'
#pattern = re.compile(r'.')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)

# literal .
#pattern = re.compile(r'\.')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)

# \d - finds any digit from 0-9
#pattern = re.compile(r'\d')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)

# \D Finds non digit from 0-9
#pattern = re.compile(r'\D')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)

#text_to_match ='''Daniel    1234 abcd
#this.thing@email.com
#this_other-thing@email.com'''

# \w finds any Word characters (a-z, A-Z, 0-9, _)
#pattern = re.compile(r'\w')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)

# \W finds any Non-Word characters
#pattern = re.compile(r'\W')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)

# \s Finds any Whitespace (space, tabs, new lines)
#pattern = re.compile(r'\s')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)

# \S Finds Non-Whitespace
#pattern = re.compile(r'\S')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)


# ******* Anchors *******
# Anchors don't match chars, match invisible positions before or after chars

#text_to_match = """lol lololol
#Daniel 1234 abcd
#this.thing@email.com
#    this_other-thing@email.com"""

# \b finds word boundaries, 
# anything prefixed with a start of a new line, start of a string, spaces, tabs
#pattern = re.compile(r'\blol')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)

# \B finds non-word boundaries
#pattern = re.compile(r'\Blol')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)

# ^ - finds matches at beginning of string
#pattern = re.compile(r'^lol')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)

# $ finds matches at end of string
#pattern = re.compile(r'com$')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)


#text_to_match = """lol lololol
#Daniel 1234 abcd
#this.thing@email.com
#    this_other-thing@email.com
#210-444-4444
#512*888*8888
#"""


#pattern = re.compile(r'\d\d\d.\d\d\d\d')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)

# [] - Character set, used to search a group of characters

#pattern = re.compile(r'\d\d\d[-*]\d\d\d[-*]\d\d\d\d')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)

# Find a range of values using - within brackets
#pattern = re.compile(r'[a-dA-D]')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)

# ^ within brackets negates those characters
#pattern = re.compile(r'[^a-dA-D]')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)

# ****** Quantifiers ******
# Match more than one character at once

#text_to_match = """lol lololol
#Daniel 1234 abcd
#this.thing@email.com
#    this_other-thing@email.com
#210-444-4444
#512*888*8888
#Mr. John
#Mr. Jim
#Mr Joe
#Mrs. Jane
#Mr. T
#"""
#pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)

# ? find 0 or 1 match
#pattern = re.compile(r'Mr\.?')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)

# + 1 or more 
#pattern = re.compile(r'Mr\.?\s[A-Z]\w+')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)

# * is 0 or more

#pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)


# Groups let us match several different patterns
# Here we can match an 'M' then an "r" or an "s" or "rs"
#pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
#matches = pattern.finditer(text_to_match)

#for match in matches:
#    print(match)

# Find emails
#emails = """
#TestUser@gmail.com
#test.user@school.edu
#test-123-user@this-place.net
#bademail@.com
#"""

# match first email
#pattern = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.com')
#matches = pattern.finditer(emails)

#for match in matches:
#    print(match)

# match other two email
#pattern = re.compile(r'[a-zA-Z.]+@[a-zA-Z]+\.(come|edu)')
#matches = pattern.finditer(emails)

#for match in matches:
#    print(match)

#pattern = re.compile(r'[a-zA-Z.0-9-]+@[a-zA-Z-]+\.(come|edu|net)')
#matches = pattern.finditer(emails)

#for match in matches:
#    print(match)


# ******Groups******

#urls = """
#http://testsite.com
#https://www.google.com
#https://youtube.com
#https://www.nasa.com
#"""

# we can group all of these to grab groups
# group 0 being all groups, then group 1 being first group...etc.
#pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
#matches = pattern.finditer(urls)

#for match in matches:
#    print(match.group(0, 1, 2, 3))

# substitute out groups 2 and 3 for our urls every time it finds a match
#pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
#subbed_url = pattern.sub(r'\2\3', urls)

#print(subbed_url)

# findall() - This returns matches as a list of strings
# If there are no groups, it returns a list of strings
# If there is one group it returns taht group as a list of strings
# If there are more than one group, it returns a list of tuples

#text_to_match = """lol lololol
#Daniel 1234 abcd
#this.thing@email.com
#    this_other-thing@email.com
#210-444-4444
#512*888*8888
#Mr. John
#Mr. Jim
#Mr Joe
#Mrs. Jane
#Mr. T
#"""

#pattern = re.compile(r'(Mr|Ms|Mrs)\.?(\s[A-Z]\w*)')
#matches = pattern.findall(text_to_match)

#for match in matches:
#    print(match)


# flags
string = 'I cAan TyPeE GoOd"'

pattern = re.compile(r'[ao]', re.I)
matches = pattern.findall(string)

for match in matches:
    print(match)