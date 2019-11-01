# This opens files
def main():
    #open file
    f = open(r'C:\Users\student\Desktop\philosiphers2.txt','w')
    #writes lines
    f.write('Name1\n')
    f.write('Name2\n')
    f.write('Name3\n')

#close files
    f.close()
main()