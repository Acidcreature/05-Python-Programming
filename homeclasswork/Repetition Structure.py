Calories Burned

#Calories burned function
def caloriesBurned():
    burn = 3.9
    minutes = [10, 15, 20, 25, 30]
    for i in minutes:
        burning = burn * i
        print(f"You burned {burning} calories.")
caloriesBurned()
################################################

#Bug Collection function
def buggrab():
    #length of collection is 7 days
    days = [1, 2, 3, 4, 5, 6, 7]
    bugs = 0
    for d in days:
        bugs += int(input("How many bugs you grab today? "))
    print("You found {} bugs".format(bugs))
buggrab()

################################################
#Budget Calculating function
def budget():
    #Users monthly budget
    MBUDGET = float(input("Please enter how broke you are each month "))
    #Continue prompt and inital variable for expenses
    continuation = input("Do you have expenses to add? Please enter 'Y' or 'N'. ")
    expensestotal = 0
    #The loop user enters in monthly expenses and recieved end result.
    while continuation == 'Y':
        expensestotal += float(input("Please enter your expenses "))
        continuation = input("Do you have expenses to add? Please enter 'Y' or 'N'. ")
    print(f"You spent {expensestotal}, and you allocated {MBUDGET}. You are left with {MBUDGET - expensestotal}")
budget()

################################################
#Distance calculator
#Initial variables and increment counter
speed = int(input("Please enter your speed rounded to the nearest 10s. ie 20, 30, 40, 60, etc. "))
time = int(input("Please enter the length of your trip in whole hours. "))
DIST = speed * time
timecount = 0
#Until timecounter and time are equal, the while loop will run.
while timecount < time:
    timecount += 1
    print(f"You traveled {speed * timecount} miles so far.\n")
print(f"{DIST} miles traveled total.")

################################################
#Celcius Table
def ctable():
    C = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    F = ""

    for i in C:
        F = (9/5) * i +32
        print(f"{F:.2f}")
ctable()
################################################
#Average Rainfall
def rainCalc():
#Find the number of years the user is calculating
    years = int(input("How many years of rainfall are you measuring? "))
    totalRain = 0
    months = 0
    while months < (years * 12):
        for m in range(years * 12):
            totalRain = int(input("Enter inches of rain per month "))
            months += 1
    print(f"The total amount of rain is {totalRain} and the average rainfall is {totalRain / months:.2f}")
###############################################
#Pennies for Pay
def pennies4Pay():
#Variables
    days = int(input("How many days are you going to work? "))
    pay = 0
    pennies = 1
    for d in range(days):
        pay += pennies
        pennies = pennies * 2
    print(f"You would be paid a total of {pay / 100} dollars")
pennies4Pay()
rainCalc()