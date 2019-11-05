#This opens a file containing integers
def main():
    #open file
    f = open('integers.txt','w+')
    #writes integers to line
    f.write(str(1) + '\n')
    f.write(str(2) + '\n')
    f.write(str(3) + '\n')

    #f.close()
    #f = open('integers.txt','r')

    #read line
    f.seek(0)
    line = f.readline()
    #as long as empty string is not returned, continue
    while line != '':
        print(line)
        line = f.readline()

#close files
    f.close()
main()