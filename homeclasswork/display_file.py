#display contents of a file
def main():
    #get name
    filename = input('Enter filename: ')
    try:
        #open file
        infile = open(filename, 'r')
        #read it
        contents = infile.read()
        #display it
        print(contents)
        #close it
        infile.close()
    except IOError:
        print("Error occured trying to read", filename)
#call main
main()