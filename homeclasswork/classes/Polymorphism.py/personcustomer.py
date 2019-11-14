# This is the Person and Customer Class

class Person:
    # The __init__ method accepts an argument for
    # the Person
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    # The following methods are mutators for the
    # class's data attributes

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    # The following methods are the accessors for the
    # class's data attributes

    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

class Customer(Person):
    # The __init__ method accepts arguments for the
    # customer id and mail list
    def __init__(self, name, address, phone, custID, maillist):
        # Call the superclass's __init__ and pass the 
        # required arguments.
        super().__init__(name, address, phone)

        # Initialize __custID and __maillist
        self.__custID = custID
        self.__maillist = maillist

    # The following methods are mutators for the
    # class's data attributes

    def set_custID(self, custID):
        self.__custID = custID

    def set_maillist(self, maillist):
        self.__maillist = maillist

    # The following methods are the accessors for the
    # class's data attributes

    def get_custID(self):
        return self.__custID
    
    def get_maillist(self):
        return self.__maillist