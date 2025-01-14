# This program demonstrates polymorphism

import animals

def main():
    # Create a Mammal object, Dog objecct, and Cat object
    mammal = animals.Mammal('regular animal')
    dog = animals.Dog()
    cat = animals.Cat()

    # Display information about each one
    print('Here are some animals and')
    print('the sounds they make.')
    print('-------------------------')
    show_mammal_info('mammal')
    print()
    show_mammal_info(dog)
    print()
    show_mammal_info(cat)

    # The show_mammal_info function accepts an object
    # as an argument and calls its show_species
    # and make_sound methods

def show_mammal_info(creature):
    if isinstance(creature, animals.Mammal):
        creature.show_species()
        creature.make_sound()
    else:
        print('That is not a mammal')

# call main
main()