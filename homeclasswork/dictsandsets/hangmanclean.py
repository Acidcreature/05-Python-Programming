import getpass

def hangman():
    guesses = 0
    guessedletters = []
    currentguess = ''
    correct = []
    incorrect = []
    gameboard = []

    print('\n')
    print("************************")
    print("*Welcome to Hang-pardy!*")
    print("************************")
    print('\n')
    print("The rules are simple. You will have 6 guesses to identify the word that has been hidden.")
    print("You can either guess a single letter, or the whole word at the end.")
    print("If you don\'t have a solution the sixth turn, you lose.", '\n')
    
    hiddenword = getpass.getpass("Please enter a word to start the game. ").lower()
    
    while hiddenword == int or hiddenword == float:
        hiddenword = input("Please enter a word to start the game. ")
    
    gameboard = ['_'] * len(hiddenword)
    
    occurences = [index for index, letter in enumerate(hiddenword) if letter == ' ']
    if occurences:
        for i in occurences:
            gameboard[i] = ' '
    
    occurences = [index for index, letter in enumerate(hiddenword) if letter == '-']
    if occurences:
        for i in occurences:
            gameboard[i] = '-'
    print(' '.join(gameboard), '\n')
    
    while guesses < 6 and '_' in gameboard:
        
        currentguess = input("Enter a letter to be guessed. ").lower()
        
        if len(currentguess) <= 1:
            while currentguess.isalpha() == False:
                currentguess = input("Enter a letter to be guessed. ")
        
            if currentguess in guessedletters:
                currentguess = input("This letter has been used, Please guess again. ")
            else:
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
    
    else:
        
        if '_' in gameboard:
            print("Time to guess the word, or else you LOSE.")
            lastchance = input("Please enter what you think the word is. ").lower()
            if lastchance == hiddenword:
                print("You Win!")
            else:
                print(f"You lost, son. The word was {hiddenword.title()}")
        
        elif '_' not in gameboard:
            print("You Win!")

hangman()