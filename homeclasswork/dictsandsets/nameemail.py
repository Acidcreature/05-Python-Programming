"""​
8. Name and Email Addresses
Write a program that keeps names and email addresses in a dictionary as key-value pairs. 
The program should display a menu that 
lets the user look up a person’s email address,
add a new name and email address,
change an existing email address, 
and delete an existing name and email address. 
The program should pickle the dictionary and save it to a file
when the user exits the program. Each time the program starts, it should retrieve the dictionary from the file and unpickle it.
​"""

import pickle


# The main function
def nameemail():
    try:
        #open file if this is not the first time the program runs
        nefileprint = open('nameemail.dat', 'rb')
        nedata = pickle.load(nefileprint)
        print(nedata)
    except:
        # Dictionary of stored names and emails
        nedata = {'Jon Snow' : 'winter1$coming@whitewalker.com', 'Bruce Wayne' : 'imB@tman@darkcave.com'}
    finally:
        # Who is the user looking for?
        entry = nedata.get(input('Please enter the name of the person you\'d like to contact via email. '))
        # Print the requested info, or none.
        print(f"Here is the information we have stored,", entry)
        print("Here are the contacts available. ", nedata)    
        # Bring the user to the selection menu.
        print("If the contact is not available, please look at the following options. \n")
        numchoice = ''
        while numchoice != 'exit':
            numchoice = input("Please select one of the following. \n \
            1. Add a new Name/Email. \n \
            2. Change an existing email. \n \
            3. Delete a Name/Email. \n \
            4. Type \'exit\' to stop. \n ")
            # First loop, add names/emails.
            while numchoice != '0' or numchoice != 'exit':
                if numchoice == '1':
                    addname = input("Please enter the Name to add. ")
                    addemail = input("Please enter the Email to add. ")
                    nedata.update({addname : addemail})
                    print('\n')
                    print(nedata)
                    print('\n')
                    #input validation
                    numchoice = input("Do you need to enter more data? Enter 1 to continue, \
                       \n 0 to go back to main menue, or \'exit\' to end. \n ")
                       
                    while numchoice != '0' and numchoice != '1' and numchoice != 'exit':
                        numchoice = input("Do you need to enter more data? Enter 1 to continue, \
                       \n 0 to go back to main menue, or \'exit\' to end. \n")
                       
                else:
                    break
                #Second loop for editting emails
            while numchoice != '0' or numchoice != 'exit':
                if numchoice == '2':
                    namechange = input("Please enter the Name you\'d like to change information of. ")
                    # If a name not in the dictionary is entered, loop continues.
                    if namechange not in nedata:
                        namechange = input("Please enter the Name you\'d like to change information of. ")
                    else:
                        # Changes are entered, added to dictionary, and print completion.
                        emailchange = input("Enter new email. ")
                        nedata.update({namechange : emailchange})
                        print('\n')
                        print(nedata)
                        print('\n')
                        #input validation
                        numchoice = input("Do you need to enter more data? Enter 2 to continue, \
                       \n 0 to go back to main menue, or \'exit\' to end. \n ")
                        while numchoice != '0' and numchoice != '2' and numchoice != 'exit':
                            numchoice = input("Do you need to enter more data? Enter 2 to continue, \
                       \n 0 to go back to main menue, or \'exit\' to end. \n ")
                else:
                    break
                #Third loop for deleting entries
            while numchoice != '0' or numchoice != 'exit':
                if numchoice == '3':
                    print(nedata)
                    #Data to delete
                    userdel = input("Enter a user name to delete ")
                    del nedata[userdel]
                    print('\n')
                    print(nedata)
                    print('\n')
                    #input validation
                    numchoice = input("Do you need to enter more data? Enter 3 to continue, \
                       \n 0 to go back to main menue, or \'exit\' to end. ")
                    while numchoice != '0' and numchoice != '3' and numchoice != 'exit':
                        numchoice = input("Do you need to enter more data? Enter 3 to continue, \
                       \n 0 to go back to main menue, or \'exit\' to end. ")
                else:
                    break
        #make file
        nefile = open('nameemail.dat', 'wb')

        #Pickling process
        #source, destination
        pickle.dump(nedata, nefile)
        nefile.close()

        #open file
        nefileprint =open('nameemail.dat', 'rb')
        nebin = pickle.load(nefileprint)
        print(nebin)

nameemail()
