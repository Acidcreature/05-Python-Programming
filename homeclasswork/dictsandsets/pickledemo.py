# Pickle Intro
# Serializing an object is the process of converting the object to a stream of bytes
# that can be saved to a file for later retrieval. In python, this is called pickling.

'''
output_file = open('mydata.dat', 'wb')
pickle.dump(object, file)
'''
# This program demonstrates object pickling
import pickle

#main function
def main():
    #controls loop repitition
    again = 'y'

    # open a file for binary writing
    output_file = open('information.dat', 'wb')

    #Get data until the user stops
    while again.lower() == 'y':
        #get data about person and save it
        save_data(output_file)

        #does the user want to enter more data?
        again = input("Enter more data? (y/n)")

    #close the file
    output_file.close()

# The save_data function gets data about a person,
# stores it in a dictionary, and then pickles the,
# dictionary to the specified file.
def save_data(file):
    # create an empty dictionary
    person = {}

    # get the data for a person and store it in a dictionary
    person['name'] = input('Name: ')
    person['age'] = input('Age: ')
    person['weight'] = float(input('Weight: '))

    person.update({'name: ': input('Name: '), 'age ': input('Age: '), 'weight': float(input('weight: '))})

    # pickle the dictionary
    pickle.dump(person, file)

# call main
main()
