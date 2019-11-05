#reads lines
def main():
    f = open(r"C:\\Users\\student\\Desktop\\philosiphers.txt",'r')
    #read individual lines
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()
    #close file
    f.close()
    print(line1)
    print(line2)
    print(line3)
    #call main
main()