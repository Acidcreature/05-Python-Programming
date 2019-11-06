# This demonstrates unpickle.
import pickle

#main function
def main():
    #indicates end of the file
    end_of_file = False

    # open a file for binary reading
    input_file = open('information.dat', 'rb')

    # read to the end of file
    while not end_of_file:
        try:
            #unpickle/deserialize the next object
            person = pickle.load(input_file)

            #display data
            display_data(person)

        except EOFError:
            #Set the flag to indicate the end of the file has been reached
            end_of_file = True

    #close file
    input_file.close()


#The display_data function displays the person data in the dictionary 
#that is passed as an argument
def display_data(person):
    print('Name ', person['name'])
    print('Age ', person['age '])
    print('weight', person['weight'])

#call the main function
main()