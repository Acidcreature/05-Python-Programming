# This program imports the coin module and
# creates an instance of the Coin class

import coin

def main():
    #create an object from Coin class
    my_coin = coin.Coin()

    # Display the side of the coin that is facing up
    print("This side is up", my_coin.get_sideup())

    #toss coin
    print("I am tossing the coin 10 times:")
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())

#Call main
main()