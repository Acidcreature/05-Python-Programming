|[Table of Contents](/00-Table-of-Contents.md)|
|---|

---

## Lab 3A

![](../.gitbook/assets/madlibs.png)

## General

Create your own mad libs game asking the user for input to fill in the blanks. Print out using .format\(\).

\(Humor encouraged\)

## Background

"Mad Libs is a phrasal template word game where one player prompts others for a list of words to substitute for blanks in a story, before reading the – often comical or nonsensical – story aloud. The game is frequently played as a party game or as a pastime."

## Requirments

* Adhere to PEP8 \(Comments, formatting, style, etc\)
* Create a handfull of pharses that require different numbers of inputs
* Prompt the user for input\(s\):
  * Inputs can be done a number of ways... 
    * \(SIMPLE\) Ask user for input directly, tell them if the word\(s\) need to be a verb, noun, etc. 
    * \(Moderate\) Give the user a handful of choices per input to choose from.You will need to create a bank of verbs, nouns, etc for this. 
    * \(Harder\) Give the user cards based off the actual game. Allowing them to draw, etc following the rules. Allow them to only input those cards. 
  * \(opitional\) Implement basic user input checking:
    * Check to ensure words are words, numbers are numbers \(there are many ways to do this\)
    * Ensure symobls aren't used if they are not needed
    * Check length
    * etc
    * Implement re-input if input is incorrect
* Output the user inputs into the given pharse
* Use formatting to not only output the user inputs, but to create a UI within the terminal. Space out certain UI elements such as title of program, choices, menu deceration, etc. 

---
```
import time
input1 = input("Do you want to create a Madlib? Select Yes or No ")
while input1 != "Yes" and input1 != "No" and input1 != "Y" and input1 != "N" and input1 != "yes" and input1 != "no"
    print("Please select Yes or No ")
    input1 = input()


Adj = input("Please enter an Adjective ")
Verb = input("Please enter a Verb ")
Noun = input("Please enter a Noun ")
Verb2 = input("Please enter another Verb ")
Day = input("Please enter a Day of the Week ")
Color = input("Please enter a Color ")
favActor = input("Please enter your favorite Actor ")

print("Please wait a moment while I generate your story")
time.sleep(10)
print("Once upon a time, there was a man named Reuben. Yes, like the sandwhich...Reuben was {}, because he didn't\
\nlike {}. One day he was struck by a {} and was given the incredible ability to {}. On {} the sky\
\nturned {} and {} proposed to the Queen of England. The End".format(Adj, Verb, Noun, Verb2, Day, Color, favActor ))

```

|[Next Topic](/03_Flow_Control/03_io_files.md)|
|---|
