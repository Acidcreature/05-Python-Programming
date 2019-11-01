#program reads all values in sales2.txt
def main():
    #open sales2.txt
    sales_file = open('sales2.txt', 'r')
    #read first line but dont convert to number yet
    line = sales_file.readline()

    #as long as empty string is not returned, continue
    while line != '':
        #convert line to float
        amount = float(line)
        #format and display
        print(format(amount, '.2f'))
        #read next line
        line = sales_file.readline()
    #close file
    sales_file.close()
#call main
main()