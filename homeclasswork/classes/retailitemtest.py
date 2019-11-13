# This program tests the Retail Item Clss
import retailitemclass as ret

def main():
    #Get a list of items
    items = items_list()

    #display the list
    print('Items on record: ')
    display_list(items)

#Make a list of items
def items_list():
    #Create empty list
    items_list = []

    # Adds information for items
    print('Item info being entered: ')
    for count in range(1, 4):
        print('Item Number ' + str(count) + ':')
        desc = input('Description: ')
        inv = input('Units in Inventory: ')
        price = float(input('Price per unit: '))
        print()

        #Create a new item object in memory
        item = ret.RetailItemClass(desc, inv, price)

        #Add object to the list
        items_list.append(item)
    #Return list
    return items_list

#Accepts a list as arg and shows data
def display_list(items_list):
    for item in items_list:
        print(item.get_desc())
        print(item.get_inv())
        print(item.get_price())
        print()

main()


