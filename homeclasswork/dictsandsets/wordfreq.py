"""
5. Word Frequency
Write a program that reads the contents of a text file. The program should create a dictionary in which the keys are the individual words 
found in the file and the values are the
number of times each word appears. For example, if the word “the” appears 128 times,
the dictionary would contain an element with 'the' as the key and 128 as the value.
The program should either display the frequency of each word or create a second file
containing a list of each word and its frequency
"""
def wordfreq():
    word_dict = {}
    #open file
    infile = open("words.txt", 'r')
    #read it and add to set
    line = infile.read().split(' ')
    #print(line)
    # add each item to the dictionary
    for e in line:
        if e not in word_dict:
            word_dict[e] = 1 
        elif e in word_dict:
            word_dict[e] += 1 
    print(word_dict)
wordfreq()