# tests car class
import carclass as car

def main():
    # get phone data
    year = input("What year is your car? ")
    make = input("What make is your car? ")
    speed = 0
    accel = 0
    brake = 0
    # instance
    drivetest = car.Cars(year, make, speed)
    #display
    print('Here is the data you entered')
    print('Manufacturer: ', drivetest.get_year())
    print('Model: ', drivetest.get_make())

    car_speed = car.Cars(year, make)

    print("Speed test begins now...")
    
    print(f"Your car is going {speed} mph. ")

    for count in range(5):
        print(f"Youre current speed is {car_speed.__accel()}")

main()


