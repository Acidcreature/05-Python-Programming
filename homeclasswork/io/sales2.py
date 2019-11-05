# Writes sales to sales.txt

def main():
    #get number of days
    num_days = int(input('How many days of sales? '))

    #open new file
    sales_file = open('sales2.txt', 'w')

    #get the sales and write to file
    for count in range(1, num_days + 1):
        #get sales for a day
        sales = float(input('Enter sales for day # ' + \
                                str(count) + ': '))
        #writes sales amount
        sales_file.write(str(sales) + '\n')

    #close file
    sales_file.close()
    print('Data written to sales2.txt')
#call main
main()