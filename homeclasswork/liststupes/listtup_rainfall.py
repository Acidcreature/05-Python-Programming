""" 3. Rainfall Statistics
Design a program that lets the user enter the total rainfall for each of 12 months into a list.
The program should calculate and display the total rainfall for the year, the average monthly
rainfall, and the months with the highest and lowest amounts. """

def rain():
    rainlist = []

    for r in range(12):
        rain = int(input("How much rain this month? "))
        rainlist.append(rain)
    raintotal = 0
    for i in rainlist:
        raintotal += i
    print(raintotal)
    print(raintotal / 12)
    print("The min rain is ", min(rainlist))
    print("The max rain is ", max(rainlist))
rain()
        
    
