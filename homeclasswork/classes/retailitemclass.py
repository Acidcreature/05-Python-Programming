#The Retail Item Class

class RetailItemClass:
    # The __init__ method initializes the attributes
    def __init__(self, desc, inv, price):
        self.__desc = desc
        self.__inv = inv
        self.__price = price


    # The get_des method returns the desc
    def get_desc(self):
        return self.__desc

    # The get_inv method returns the inv
    def get_inv(self):
        return self.__inv

    # The get_price method returns the price
    def get_price(self):
        return self.__price
