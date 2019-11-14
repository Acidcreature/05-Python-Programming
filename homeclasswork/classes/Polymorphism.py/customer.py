# This program is a test of the Customer Class

import personcustomer

def main():
    # Create an object
    cust1 = personcustomer.Customer('Karen', '123 Google', 'N/A', '12345', False)

    # Display the customers data
    print('Name: ', cust1.get_name())
    print('Address: ', cust1.get_address())
    print('Phone: ', cust1.get_phone())
    print('CustID: ', cust1.get_custID())
    print('Are they on the mail list?: ', cust1.get_maillist())

main()