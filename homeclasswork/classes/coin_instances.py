# This program imports the simulation module and
# creates three instances of the Coin class

import coin

def main():
    # create three objects from the Coin class
    coin1 = coin.Coin()
    coin2 = coin.Coin()
    coin3 = coin.Coin()

    # Display the side of each coin that is facing up
    print('I have three coins with these sides up:')
    print('coin1:',coin1.get_sideup())
    print('coin2:',coin2.get_sideup())
    print('coin3:',coin3.get_sideup())

    # Toss the coin
    print('I am tossing all three coins..')
    print()
    coin1.toss()
    coin2.toss()
    coin3.toss()

    # Display the side of each coin that is now facing up
    print('I have three coins with these sides up:')
    print('coin1:',coin1.get_sideup())
    print('coin2:',coin2.get_sideup())
    print('coin3:',coin3.get_sideup())
    print()

# call main
main()