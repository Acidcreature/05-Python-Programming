# The Pet class
class PetClass:
    # the __init__ method intializes
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

        # The set_name method accepts an arguement for the name
    def set_name(self, name):
        self.__name = name

    # The set_animal_type method accepts an argument for the type
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
    
    # The set_age method accepts an argument for the age
    def set_age(self, age):
        self.__age = age

    # The get_name method returns the phone's manufacturer
    def get_name(self):
        return self.__name
    
    # The get_animal_type method returns the type
    def get_animal_type(self):
        return self.__animal_type

    # The get_age method returns the age
    def get_age(self):
        return self.__age