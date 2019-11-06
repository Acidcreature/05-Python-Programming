"""
Write a program that reads the contents of two text files and compares them in the following ways:
• It should display a list of all the unique words contained in both files.
• It should display a list of the words that appear in both files.
• It should display a list of the words that appear in the first file but not the second.
• It should display a list of the words that appear in the second file but not the first.
• It should display a list of the words that appear in either the first or second file but not both.
Hint: Use set operations to perform these analyses.
"""
def fileanalysis():

    word_dict1 = {}
    #open file
    infile = open("words.txt", 'r')
    #read it and add to set
    line = infile.read().split(' ')
    #print(line)
    # add each item to the dictionary
    for e in line:
        if e not in word_dict1:
            word_dict1[e] = 1 
        elif e in word_dict1:
            word_dict1[e] += 1 
    print(word_dict1)

    word_dict2 = {}
    #open file
    infile = open("names.txt", 'r')
    #read it and add to set
    line = infile.read().split(' ')
    #print(line)
    # add each item to the dictionary
    for e in line:
        if e not in word_dict2:
            word_dict2[e] = 1 
        elif e in word_dict2:
            word_dict2[e] += 1 
    print(word_dict2)







