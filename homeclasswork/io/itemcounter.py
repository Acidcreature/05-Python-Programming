#Read names.txt and count number of names
def main():
    #get name
    file = open('names.txt','r')
    #read that file 
    line = file.readline()
    #print(line)
    linecount = 0
    while line != '':
        linecount += 1
        #print(linecount)
        line = file.readline()
    print(linecount)
    #close file
    file.close()
main()