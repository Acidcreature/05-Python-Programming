# This program tests the CellPhone class

import cellphone as c

def main():
    # get the phone data.
    man = input('Enter the manufacturer: ')
    mod = input('Enter the model: ')
    retail = float(input('Enter the retail price: '))

    # Creates an instance of the cellphone class
    phone = c.CellPhone(man, mod, retail)

    # display the data that was entered
    print('Here is the data you entered')
    print('Manufacturer: ', phone.get_manufact())
    print('Model: ', phone.get_model())
    print(f'Retail Price: ${phone.get_price():,.2f}')

# Calls main
main()