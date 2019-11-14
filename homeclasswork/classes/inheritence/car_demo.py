# This program demonstrats the Car class

import vehicle

def main():
    # Create an object from the Car class
    # The car is a 2007 Audi with 12k miles, priced at
    # 21.5k and has 4 doors.
    used_car = vehicle.Car('Audi', 'A3', 12500, 21500.00, 4)

    # Display the cars data
    print('Make: ', used_car.get_make())
    print('Model: ', used_car.get_model())
    print('Mileage: ', used_car.get_mileage())
    print('Price: ', used_car.get_price())
    print('Doors: ', used_car.get_doors())
# Call the main function
main()