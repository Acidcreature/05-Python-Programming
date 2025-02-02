# this program demonstrates the range sum function

def main():
    # Create a list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # get the sum of the items at indexes 2 through 5
    my_sum = range_sum(numbers, 2, 5)

    # display sum
    print('The sum of items 2 throguh 5 is', my_sum)

# the range_sum function returns the sum of a specified 
# range of items in num_list. The start parameter
# specifies the index of the starting item, The end
# parameter specifies the index of the ending item
def range_sum(num_list, start, end):
    if start > end:
        #base case
        return 0
        # recursive case
    else:
        return num_list[start] + range_sum(num_list, start + 1, end)

# call main
main()
