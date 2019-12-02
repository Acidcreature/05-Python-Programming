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



#############################################################################################

#'''Import random'''
#import random
#​
#'''Global List'''
#matrix = []
#​
#'''Main Function'''
#def main():
#    matrix_generator()
#    for i in matrix:
#        print(i)
#    row = row_counter(matrix)
#    column = column_counter()
#    print(f"Rows(s) with the highest value: {row}")
#    print(f"Column(s) with the highest value: {column}")
#​
#'''Generates a matrix of random values'''
#def matrix_generator():
#    rand = random.randint(2,11)
#    for i in range(0,rand):
#        matrix.append([])
#    for i in range(0,rand):
#        for j in range(0, rand):
#            matrix[j].append(random.randint(0,1))
#​
#'''Used to generate the row. Will also be used on columns'''
#def row_counter(matrix):
#    row = [0]
#    for i in range(len(matrix)):
#        j = sum(matrix[i])
#        k = row[0]
#        if j > sum(matrix[k]):
#            row = []
#            row.append(i)
#        elif j == sum(matrix[k]) and i != 0:
#            row.append(i)
#    return row
#​
#'''Inverts list then utilizes row function to calculate total.'''
#def column_counter():
#    column_list = []
#    x = 0
#    while x < len(matrix):
#        '''This new list will be used to invert the matrix'''
#        new_list = []
#        y = 0
#        while y < len(matrix):
#            if matrix[y][x] == 1:
#                new_list.append(1)
#            else:
#                new_list.append(0)
#            y += 1
#        column_list.append(new_list)
#        x += 1
#    return row_counter(column_list)
#​
#'''Call on the main function'''
#main()