# The Personal Information Class

class Pii:
    # the __init__ method initializes the attributes
    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    # The set_name method accepts an arguement for the name
    def set_name(self, name):
        self.__name = name

    # The get_name method returns the name
    def get_name(self):
        return self.__name

    # The set_address method accepts an arguement for the address
    def set_address(self, address):
        self.__address = address

    # The get_year method returns the address
    def get_address(self):
        return self.__address

    # The set_age method accepts an arguement for the age
    def set_age(self, age):
        self.__age = age

    # The get_age method returns the age
    def get_age(self):
        return self.__age

    # The set_phone method accepts an arguement for the phone
    def set_phone(self, phone):
        self.__phone = phone

    # The get_age method returns the age
    def get_phone(self):
        return self.__phone