"""2. Capital Quiz
Write a program that creates a dictionary containing the U.S. states as keys and their capitals as values. 
(Use the Internet to get a list of the states and their capitals.) The program
should then randomly quiz the user by displaying the name of a state and asking the user
to enter that state’s capital. The program should keep a count of the number of correct and
incorrect responses. (As an alternative to the U.S. states, the program can use the names of
countries and their capitals.)
"""

import random

def capquiz():
# Dict of all states and capitals
    capital_dict = {
        1:{'Alabama': 'Montgomery'},
        2:{'Alaska': 'Juneau'},
        3:{'Arizona':'Phoenix'},
        4:{'Arkansas':'Little Rock'},
        5:{'California': 'Sacramento'},
        6:{'Colorado':'Denver'},
        7:{'Connecticut':'Hartford'},
        8:{'Delaware':'Dover'},
        9:{'Florida': 'Tallahassee'},
        10:{'Georgia': 'Atlanta'},
        11:{'Hawaii': 'Honolulu'},
        12:{'Idaho': 'Boise'},
        13:{'Illinios': 'Springfield'},
        14:{'Indiana': 'Indianapolis'},
        15:{'Iowa': 'Des Monies'},
        16:{'Kansas': 'Topeka'},
        17:{'Kentucky': 'Frankfort'},
        18:{'Louisiana': 'Baton Rouge'},
        19:{'Maine': 'Augusta'},
        20:{'Maryland': 'Annapolis'},
        21:{'Massachusetts': 'Boston'},
        22:{'Michigan': 'Lansing'},
        23:{'Minnesota': 'St. Paul'},
        24:{'Mississippi': 'Jackson'},
        25:{'Missouri': 'Jefferson City'},
        26:{'Montana': 'Helena'},
        27:{'Nebraska': 'Lincoln'},
        28:{'Neveda': 'Carson City'},
        29:{'New Hampshire': 'Concord'},
        30:{'New Jersey': 'Trenton'},
        31:{'New Mexico': 'Santa Fe'},
        32:{'New York': 'Albany'},
        33:{'North Carolina': 'Raleigh'},
        34:{'North Dakota': 'Bismarck'},
        35:{'Ohio': 'Columbus'},
        36:{'Oklahoma': 'Oklahoma City'},
        37:{'Oregon': 'Salem'},
        38:{'Pennsylvania': 'Harrisburg'},
        39:{'Rhode Island': 'Providence'},
        40:{'South Carolina': 'Columbia'},
        41:{'South Dakoda': 'Pierre'},
        42:{'Tennessee': 'Nashville'},
        43:{'Texas': 'Austin'},
        44:{'Utah': 'Salt Lake City'},
        45:{'Vermont': 'Montpelier'},
        46:{'Virginia': 'Richmond'},
        47:{'Washington': 'Olympia'},
        48:{'West Virginia': 'Charleston'},
        49:{'Wisconsin': 'Madison'},
        50:{'Wyoming': 'Cheyenne'}
        }
#Get random number
    again = input("Play state quiz? 'y' or 'n'. ")
    if again == 'y' or again == 'Y':
        r = random.randint(1, 50)
        answer = input(f"What is the capital for {capital_dict[r].keys()}"\
            f"\nEnter your answer: ")
#print(input("Please enter your answer: "))
    else:
        print("Bye")
# Verify the answer
    if again == 'y' or again == 'Y':
        if answer in capital_dict[r].values():
            print("Correct", capital_dict[r].values())
        if answer not in capital_dict[r].values():
            print("Wrong", capital_dict[r].values())
    
capquiz()
