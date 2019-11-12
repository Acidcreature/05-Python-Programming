# This program passes a coin object as 
# an argument to a function
import coin

#main function
def main():
    #create a coin object
    my_coin = coin.Coin()

    # This wil display "Heads"
    print(my_coin.get_sideup())

    # Pass the object to flip function
    flip(my_coin)

    #This might display Heads or Tails
    print(my_coin.get_sideup())

#The flip function flips a coin
def  flip(coin_obj):
    coin_obj.toss()

#call main
main()
