# Tests pii class
import piiclass as p 

# start of main function
def main():
    print('Please enter the user information')
    name = input('Name: ')
    address = input('Address: ')
    age = input('Age: ')
    phone = input('Phone: ')

    #make instance
    user1 = p.Pii(name, address, age, phone)
    
    #returns the information for verification.
    print("Please verify the information entered.")
    print('Name: ',user1.get_name())
    print('Address: ',user1.get_address())
    print('Age: ',user1.get_age())
    print('Phone: ',user1.get_phone())

    print('Please enter the user information')
    name = input('Name: ')
    address = input('Address: ')
    age = input('Age: ')
    phone = input('Phone: ')

    #make instance
    user2 = p.Pii(name, address, age, phone)
    
    #returns the information for verification.
    print("Please verify the information entered.")
    print('Name: ',user2.get_name())
    print('Address: ',user2.get_address())
    print('Age: ',user2.get_age())
    print('Phone: ',user2.get_phone())

    print('Please enter the user information')
    name = input('Name: ')
    address = input('Address: ')
    age = input('Age: ')
    phone = input('Phone: ')

    #make instance
    user3 = p.Pii(name, address, age, phone)
    
    #returns the information for verification.
    print("Please verify the information entered.")
    print('Name: ',user3.get_name())
    print('Address: ',user3.get_address())
    print('Age: ',user3.get_age())
    print('Phone: ',user3.get_phone())

    



#call main
main()
