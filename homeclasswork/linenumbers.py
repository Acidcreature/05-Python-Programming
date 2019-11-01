#Write a program that asks the user for the name of a file. 
#The program should display the contents of the file with each line 
#preceded with a line number followed by a colon. 
#The line numbering should start at 1.
def main():
    #get name
    filename = input('Enter filename: ')
    #open that file
    infile = open(filename, 'r')
    #read that file 
    line = infile.readline()
    linecount = 1
    while line != '':
        print(str(linecount) + ":" + line)
        linecount += 1
        line = infile.readline()
    #close file
    infile.close()
main()
