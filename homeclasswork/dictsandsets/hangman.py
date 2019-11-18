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

import getpass


def hangman():
    #variables for the game
    guesses = 0
    guessedletters = []
    currentguess = ''
    correct = []
    incorrect = []
    gameboard = []
    
    # the magic sauce for finding *all* occurences of a word
    # since gameboard and the word will have the same number of elements
    # we just iterate over the word and if a the condition is met we record
    # the index and toss it in a list #Cammarata
    #occurences = [i for i, v in enumerate(hiddenword) if v == currentguess]

    print('\n')
    print("*****************************")
    print("*Welcome to Hang-of-Fortune!*")
    print("*****************************")
    print('\n')
    print("The rules are simple. You will have 6 guesses to identify the word that has been hidden.")
    print("You can either guess a single letter, or the whole word at the end.")
    print("If you don\'t have a solution the sixth turn, you lose.", '\n')
    #select the word to be guessed, getpass makes it hidden from the prompt. Stops cheaters.
    hiddenword = getpass.getpass("Please enter a word to start the game. ").lower()
    #makes sure its a word
    while hiddenword == int or hiddenword == float:
        hiddenword = input("Please enter a word to start the game. ")
    # shows hidden length of word
    gameboard = ['_'] * len(hiddenword)
    #removes '_' if it should be a blank space.
    occurences = [index for index, letter in enumerate(hiddenword) if letter == ' ']
    if occurences:
        for i in occurences:
            gameboard[i] = ' '
    # same as above, but accounts for hypenated words
    occurences = [index for index, letter in enumerate(hiddenword) if letter == '-']
    if occurences:
        for i in occurences:
            gameboard[i] = '-'
    print(' '.join(gameboard), '\n')
    # Loop for guessing, with validation for letters only.
    while guesses < 6 and '_' in gameboard:
        # makes input lower, avoids conflicts with upper vs. lower for words and guesses
        currentguess = input("Enter a letter to be guessed. ").lower()
        #restricts guesses to 1 letter at a time.
        if len(currentguess) <= 1:
            while currentguess.isalpha() == False:
                currentguess = input("Enter a letter to be guessed. ")
        # Removes posibility of using a duplicate letter
            if currentguess in guessedletters:
                currentguess = input("This letter has been used, Please guess again. ")
            else:
    # the magic sauce for finding *all* occurences of a word
    # since gameboard and the word will have the same number of elements
    # we just iterate over the word and if a the condition is met we record
    # the index and toss it in a list #Cammarata
                occurences = [index for index, letter in enumerate(hiddenword) if letter == currentguess]
                if occurences:
                    for i in occurences:
                        gameboard[i] = currentguess
                    correct += currentguess
                    print('\n')
                    print(f"Correct letters so far {correct}" )
                else:
                    incorrect += currentguess
                    print('\n')
                    print(f"Incorrect letters so far {incorrect}" )
                guessedletters += currentguess
                guesses += 1
                print('\n')
                print(f"You have guessed {guessedletters} so far.")
                print("You have {} turns remaining.".format(6 - guesses))
                print('\n')
                print(' '.join(gameboard), '\n')
    # Win/Loss conditions
    else:
        # If you ran out of guesses you can still guess the word, or you lose.
        if '_' in gameboard:
            print("Time to guess the word, or else you LOSE.")
            lastchance = input("Please enter what you think the word is. ").lower()
            if lastchance == hiddenword:
                print("You Win!")
            else:
                print(f"You lost, son. The word was {hiddenword.title()}")
        # If you guessed all the letters, win.
        elif '_' not in gameboard:
            print("You Win!")


hangman()
