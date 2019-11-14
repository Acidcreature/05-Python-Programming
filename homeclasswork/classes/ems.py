import pickle
import employeeclass as emp
import employeetest as et


# The main function
def ems():
    try:
        #open file if this is not the first time the program runs
        empfileprint = open('employed.dat', 'rb')
        empdata = pickle.load(empfileprint)
        print(empdata)
    except:

        empdata = {employee.get_ID() : {'Name' : employee.get_name(), 'Dep' : employee.get_dep(), 'Job' : employee.get_job()}}
        print(emptdata)


        # Dictionary of stored names and emails
        #empdata = {'47899' : {'Name' : 'Susan Meyers','Department' : 'Accounting', 'Job Title' :'Vice President'},
        #    '39119' : {'Name' : 'Mark Jones', 'Department' : 'IT', 'Job Title' : 'Programmer'},
        #    '81774' : {'Name' : 'Joy Rogers', 'Department' : 'Manufacturing', 'Job Title' : 'Engineer'}}
        
    # Does this no matter outcome of try/except
    #finally:
        # Bring the user to the selection menu.
        print("Please look at the following options. \n")
        numchoice = ''
        while numchoice != 'exit':
            numchoice = input("Please select one of the following. \n \
            1. Lookup an employee. \n \
            2. Add a new employee. \n \
            3. Edit employee info. \n \
            4. Delete an employee. \n \
            5. Type \'exit\' to stop. \n ")
            # First loop, look up.
            while numchoice != '0' or numchoice != 'exit':
                if numchoice == '1':
                    look = input("Please enter the ID to find. ")
                    if look in empdata:
                        print(empdata[look])
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
                    addname = input("Please enter the Name of the employee. ")
                    addID = input("Please enter the ID of the employee. ")
                    adddep = input("Please enter the Department of the employee. ")
                    addjob = input("Please enter the Job of the employee. ")
                    empdata.update({addID : { 'Name' : addname, 'Department' : adddep, 'Job Title' : addjob}})
                    #input validation
                    numchoice = input("Do you need to enter more data? Enter 2 to continue,\
                    \n or 0 to go back to main menue, or \'exit\' to end. \n ")
                    while numchoice != '0' and numchoice != '2' and numchoice != 'exit':
                        numchoice = input("Do you need to enter more data? Enter 2 to continue,\
                    \n or 0 to go back to main menue, or \'exit\' to end. \n ") 
                else:
                    break
                #Third loop for changing entries
            while numchoice != '0' or numchoice != 'exit':
                if numchoice == '3':
                    userdel = input("Enter ID for user to change. ")
                    del empdata[userdel]
                    addname = input("Please enter the Name of the employee. ")
                    addID = input("Please enter the ID of the employee. ")
                    adddep = input("Please enter the Department of the employee. ")
                    addjob = input("Please enter the Job of the employee. ")
                    empdata.update({addID : { 'Name' : addname, 'Department' : adddep, 'Job Title' : addjob}})
                    #input validation
                    numchoice = input("Do you need to enter more data? Enter 3 to continue, \
                       \n 0 to go back to main menue, or \'exit\' to end. ")
                    while numchoice != '0' and numchoice != '3' and numchoice != 'exit':
                        numchoice = input("Do you need to enter more data? Enter 3 to continue, \
                       \n 0 to go back to main menue, or \'exit\' to end. ")
                else:
                    break
            while numchoice != '0' or numchoice != 'exit':
                if numchoice == '4':
                    userdel = input("Enter ID for user to be deleted. ")
                    del empdata[userdel]
                    numchoice = input("Do you need to enter more data? Enter 4 to continue, \
                       \n 0 to go back to main menue, or \'exit\' to end. ")
                    while numchoice != '0' and numchoice != '4' and numchoice != 'exit':
                        numchoice = input("Do you need to enter more data? Enter 4 to continue, \
                       \n 0 to go back to main menue, or \'exit\' to end. ")
                else:
                    break
        #make file
        empfile = open('employed.dat', 'wb')
        #Pickling process
        #source, destination
        pickle.dump(empdata, empfile)
        empfile.close()
        #open file
        empfileprint = open('employed.dat', 'rb')
        empbin = pickle.load(empfileprint)
        print(empbin)
ems()