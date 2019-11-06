"""
4. Unique Words
Write a program that opens a specified text file and then displays a list of all the unique
words found in the file.
Hint: Store each word as an element of a set
"""

def uniquewords():
    uniqueset = set()
    #Ask use for file to open.
    filename = input('Enter filename: ')
    #open file
    infile = open(filename, 'r')
    #read it and add to set
    line = infile.readline().strip("\n")
    while line != '':
        #print(line)
        uniqueset.add(line)
        line = infile.readline().strip("\n")
    print(uniqueset)
    #close it
    infile.close()
uniquewords()