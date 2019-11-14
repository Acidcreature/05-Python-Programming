# This program creates a Car object, A Truck Object, and SUV object.

import vehicle

def main():
    # Creates a Car Object
    car = vehicle.Car('Bugatti', 'Veyron', 0, 3000000, 2)
    
    # Creates a Truck object
    truck = vehicle.Truck('Dodge', 'Power Wagon', 0, 57000, '4x4')

    # Creates a SUV object
    suv = vehicle.SUV('Jeep', 'Wrangler', 200000, 5000, 4)

    print('Vehcile Inventory')
    print('*****************')

    # Display the vehicles's data
    print('Make: ', car.get_make())
    print('Model: ', car.get_model())
    print('Mileage: ', car.get_mileage())
    print('Price: ', car.get_price())
    print('Doors: ', car.get_doors())
    print('\n')
    print('Make: ', truck.get_make())
    print('Model: ', truck.get_model())
    print('Mileage: ', truck.get_mileage())
    print('Price: ', truck.get_price())
    print('Drive Type: ', truck.get_drive_type())
    print('\n')
    print('Make: ', suv.get_make())
    print('Model: ', suv.get_model())
    print('Mileage: ', suv.get_mileage())
    print('Price: ', suv.get_price())
    print('Pass Cap: ', suv.get_pass_cap())
# Call the main
main()