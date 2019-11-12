import random

# The coin class simulates a codr that can be flipped

class Coin:

    # the __init__ method initializes the sideup data attribute with "Heads"
    def __init__(self):
        self.__sideup = "Heads"

    # The toss method generates a random number
    # in the range of 0 - 1, if the number is
    # 0, then sidedup is set to heads,
    #otherwie sideup is set to tails
    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    # The get_sideup method returns the value
    # references by sideup.
    def get_sideup(self):
        return self.__sideup

# The main function
def main():
    # Create an object from the coin class.
    my_coin = Coin()
    print(type(my_coin))

    #display the side of the coin that is facing up
    print("This side is up:", my_coin.get_sideup())

    #Toss the coin
    print("I am tossing the coin...")
    #my_coin.toss
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())

    #Display the side of the coin that is facing up
    print("This side is now up:", my_coin.get_sideup())

    # sodeup attribute is not private
    my_coin.sideup = "Tails"

main()