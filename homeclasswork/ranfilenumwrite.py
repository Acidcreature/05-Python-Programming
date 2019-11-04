#writes random numbers to a file between 1-100.
import random
def rnfw():
    #how many numbers to be written
    totnum = int(input("How many random numbers? "))

    #open file
    f = open('rnfw.txt','w+')
    #writes lines
    linecount = 0
    while linecount < totnum:
        f.write(str(random.randrange(1, 100)))
        f.write('\n')
        linecount += 1
    #close file()
    f.close()
rnfw()