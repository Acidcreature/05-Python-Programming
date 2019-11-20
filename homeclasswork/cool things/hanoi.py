# Towers of Hanoi

# rules
#   Only one disk may be moved at a time
#   A dis cannot be placed on top of a smaller disc
#   all discs must be stored on a peg except while being moved
#   You must moved all discs from the first peg to the third peg

# This program simulates the Towers of Hanoi game
def main():
    # Set initial values
    num_discs = 6
    from_peg = 1
    to_peg = 3
    temp_peg = 2

    # play the game
    move_discs(num_discs, from_peg, to_peg, temp_peg)
    print('All the discs are moved')


# the moveDiscs function displays a disc move in
# the Towers of Hanoi game
# the parameters are:
#   num:        the number of discs to move
#   from_peg:   the peg to move from
#   to_peg:     the peg to move to
#   temp_peg:   the temporary peg
def move_discs(num, from_peg, to_peg, temp_peg):
    if num > 0:
        move_discs(num - 1, from_peg, temp_peg, to_peg)
        print('Move a disc from peg', from_peg, 'to peg', to_peg)
        move_discs(num - 1, temp_peg, to_peg, from_peg)

# call main
main()

