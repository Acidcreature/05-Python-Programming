# tests PetClass
import petclass as pc 

def main():
    # get info
    name = input('enter the name ')
    animal_type = input('What type of pet do you have ')
    age = input('enter the age ')

    # creates instance
    pet = pc.PetClass(name, animal_type, age)

    # display the data that was entered
    print('Here is the data you entered ')
    print('name: ', pet.get_name())
    print('animal_type: ', pet.get_animal_type())
    print('Age: ',pet.get_age())

#call main
main()