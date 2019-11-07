"""
Task:
    Your task is to implement the Hangman game in Python.
​
Program Specifications:
    1) Output a brief description of the game of hangman and how to play
    2) Ask the user to enter the word or phrase that will be guessed (have a friend enter the phrase 
        for you if you want to be surprised)
    3) Output the appropriate number of dashes and spaces to represent the phrase (make sure it’s clear 
        how many letters are in each word and how many words there are)
    4) Continuously read guesses of a letter from the user and fill in the corresponding blanks if the 
        letter is in the word, otherwise report that the user has made an incorrect guess.
    5) Each turn you will display the phrase as dashes but with any already guessed letters filled in, 
        as well as which letters have been incorrectly guessed so far and how many guesses the user has remaining.
    6) Your program should allow the user to make a total of k=6 guesses.
​
Assignment Notes:
If the letter has already been guessed, output a message to the player and ask for input again.
If the guess entered is not an alphabetic letter, output a message and ask for input again.
​
If the letter is present in the word to be guessed, fill in the blanks appropriately with this particular letter. 
If the complete name has been guessed, the game is over  - player wins the game.  Output a message telling the 
player they have won and quit the game.
​
If the letter/digit is not present in the word to be guessed, give a message to the player indicating that the 
guess is incorrect and remaining number of chances is one less. If remaining number of chances is 0 (zero), 
the game is over  - player loses the game. Output a message that they have lost and what the correct word was.  Quit the game.
"""

import time
import pprint


def hangman():
    #variables for the game
    guesses = 0
    guessedletters = []
    currentguess = ''
    correct = []
    incorrect = []
    

    print("*********************")
    print("*Welcome to Hangman!*")
    print("*********************")
    print('\n\n')
    print("The rules are simple. You will have 6 guesses to identify the word that has been hidden.")
    print("You can either guess a single letter or the whole word.")
    print("If you don\'t have a solution the sixth turn, you lose.", '\n')
    #select the word to be guessed
    hiddenword = input("Please enter a word to start the game. ")
    #makes sure its a word
    while hiddenword == int or hiddenword == float:
        hiddenword = input("Please enter a word to start the game. ")
    # shows hidden length of word
    print((" _ ") * len(hiddenword))

    while guesses < 7:
        currentguess = input("Enter a letter to be guessed. ")
        while currentguess.isalpha == False:
            currentguess = input("Enter a letter to be guessed. ")
        else:
            if currentguess in hiddenword:
                correct += currentguess
                guessedletters += currentguess
                guesses += 1
            elif currentguess not in currentguess:
                incorrect += currentguess
                guessedletters += currentguess
                guesses += 1
            print(f"You have guessed {guessedletters} so far.")
            print("You have {} turns remaining.".format(6 - guesses))
                  



hangman()
