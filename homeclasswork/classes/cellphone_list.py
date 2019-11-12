# This program creates the five CellPhone objects and
# stores them in a list

import cellphone

def main():
    # Get a list of CellPhone
    phones = make_list()

    # Display the data in the list
    print('Here is the data you entered: ')
    display_list(phones)

# The make_list function gets the data from the user
# for five phones. The function returns a list
# of CellPhone objects containing the data.
def make_list():
    # create an empty list
    phone_list = []

    # Add five cellphone objects to the list
    print('Enter data for five phones. ')
    for count in range(1, 6):
        #get the phone data
        print('Phone Number ' + str(count) + ':')
        man = input('Manufacturer: ')
        mod = input('Model: ')
        price = float(input('Price: '))
        print()

        # Create a new CellPhone object in memory then
        # assign it to the new phone variable
        phone = cellphone.CellPhone(man, mod, price)

        # Add the object to the list
        phone_list.append(phone)
    
    #Return the list
    return phone_list

# The display_list function accepts a list containing
# CellPhone objects as an argument and displays the 
# data stored in each object
def display_list(phone_list):
    for phone in phone_list:
        print(phone.get_manufact())
        print(phone.get_model())
        print(phone.get_price())
        print()

main()