"""4. Number Analysis Program
Design a program that asks the user to enter a series of 20 numbers. The program should
store the numbers in a list and then display the following data:
• The lowest number in the list
• The highest number in the list
• The total of the numbers in the list
• The average of the numbers in the list"""

def nap():
    usernums = []
    for i in range(20):
        nums = int(input("Please enter a number. "))
        usernums.append(nums)
    totalnum = 0
    for e in usernums:
        totalnum += e
    print(max(usernums))
    print(min(usernums))
    print(totalnum)
    print(totalnum / 12)
nap()