# The Car Class

class Cars:
    #the __init__ method initializes the attributes
    def __init__(self, year, make):
        self.__year = year 
        self.__make = make
        self.__speed = 0

    # The set_year method accepts an arguement for the year
    def set_year(self, year):
        self.__year = year

    # The set_make method accepts an argument for the make
    def set_make(self, make):
        self.__make = make
    
    # The set_speed method accepts an argument for the speed
    def set_speed(self, speed):
        self.__speed = speed

    # The get_year method returns the year
    def get_year(self):
        return self.__year
    
    # The get_make method returns the make
    def get_make(self):
        return self.__make

    # The get_speed method returns the speed
    def get_speed(self):
        return self.__speed

    # the set_accel method
    def set_accel(self, accel=5):
        self.__speed += accel 
    
    # the set_brake method
    def set_brake(self, brake=5):
        self.__speed -= brake

    # the get_accel method
    def get_accel(self):
        return self.__speed 

    # the get_brake method
    def get_brake(self):
        return self.__speed 