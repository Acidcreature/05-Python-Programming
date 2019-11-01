#Program asks user for name of file, diplay first 5 lines of file
def main():
    #get name
    filename = input('Enter filename: ')
    #open that file
    infile = open(filename, 'r')
    #read that file 
    line = infile.readline()
    linecount = 1
    while line != '' and linecount <= 5:
        print(line)
        linecount += 1
        line = infile.readline()
    #close file
    infile.close()
main()

