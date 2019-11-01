#Read numbers.txt and counts the total sum of numbers
def main():
    #file name
    file = open('numbers.txt','r')
    #read that file 
    line = file.readline()
    numsum = 0
    while line != '':
        numsum += int(line)
        #print(numsum)
        line = file.readline()
    print(numsum)
    #close file
    file.close()
main()