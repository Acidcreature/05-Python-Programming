#reads rannumfile, counts sum and total lines
def rnfr():
    #open file
    f = open('rnfw.txt','r')
    #read that file 
    line = f.readline()
    linecount = 0
    sumnum = 0
    while line != '':
        sumnum += int(line)
        linecount += 1
        line = f.readline()
    print(f'Total of random numbers is {linecount} and the sum of numbers are \
    {sumnum}.')
    #close file()
    f.close()
rnfr()