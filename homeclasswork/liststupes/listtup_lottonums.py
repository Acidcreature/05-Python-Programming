""" 2. Lottery Number Generator
Design a program that generates a seven-digit lottery number. The program should generate seven random numbers, 
each in the range of 0 through 9, and assign each number to a list element. 
Then write another loop that displays the contents of the list."""


import random

def lotto():
    lottolist = [0,0,0,0,0,0,0]
    for l in range(len(lottolist)):
        lottolist[l] = (random.randrange(0, 9))
    print(lottolist)

lotto()