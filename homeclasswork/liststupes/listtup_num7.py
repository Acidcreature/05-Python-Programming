"""(Largest rows and columns) Write a program that randomly fills in 0s and 1s into
a matrix, prints the matrix, and finds the rows and columns with the most
1s. Here is a sample run of the program:
0011
0011
1101
1010
The largest row index: 2
The largest column index: 2, 3"""

import random

def seven():
    firstlist = []
    listoflists = []

    #create the random lists of 1's and 0's

    # Creates a list of16 occurences of 0 or 1
    for x in range(16):
        r = random.randint(0, 1)
        firstlist.append(r)
        #When there are 4 items in a list, append that list to listoflists
        if len(firstlist) == 4:
            listoflists.append(firstlist)
            #print(firstlist)
            firstlist = []
    #print each list, creating visual columns and rows
    for e in listoflists:
        print(e)
    #setting variables to name each row
    row1 = (listoflists[0][0:])
    row2 = (listoflists[1][0:])
    row3 = (listoflists[2][0:])
    row4 = (listoflists[3][0:])
    #sum of each 1 in the row
    totalrow1 = sum(row1)
    totalrow2 = sum(row2)
    totalrow3 = sum(row3)
    totalrow4 = sum(row4)
    #prints totals
    print(totalrow1)
    print(totalrow2)
    print(totalrow3)
    print(totalrow4)
    print(f"The row with the most is {max(totalrow1, totalrow2, totalrow3, totalrow4)}")
    #column?
    print(listoflists[0][0])
    print(listoflists[0][1])
    print(listoflists[0][2])
    print(listoflists[0][3])

seven()