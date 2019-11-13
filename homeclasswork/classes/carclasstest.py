# tests car class
import carclass as car
import time


def main():
    # get data
    year = input("What year is your car? ")
    make = input("What make is your car? ")
    accel = 0
    brake = 0
    # instance
    drivetest = car.Cars(year, make)
    #display data entered
    print('Here is the data you entered')
    print('Manufacturer: ', drivetest.get_year())
    print('Model: ', drivetest.get_make())

    print("Speed test begins now...")
    #Iterate through __speed
    for count in range(5):
        drivetest.set_accel()
        print(f"Youre current speed is {drivetest.get_accel()}")
        time.sleep(1)
    print("HIT THE BRAAAAAAAAAAAAAAAKES!")
    time.sleep(2)
    for count in range(5):
        print(f"Youre current speed is {drivetest.get_brake()}")
        drivetest.set_brake()
        time.sleep(1)
    print("Speed test complete")
main()


