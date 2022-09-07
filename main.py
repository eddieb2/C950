####################################################

# STUDENT INFORMATION
# Name: Edward Andrew Blanciak
# Student ID: #001518541

# PROGRAM INFORMATION
# Overall Time Complexity - Worst Case: O(n^2)
# Overall Space Complexity - Worst Case: O(n)

####################################################

import datetime
from classes.hub import Hub
from cli import user_interface
from delivery_algorithm import  package_delivery

def main():
    # Hub Creation: Creates a hub where the packages will be stored.
    main_hub = Hub()

    # Packages: Creates and stores packages from file.
    package_data = "C:\\Users\eddie\Desktop\C950 project\data\package_data.csv"
    main_hub.add_packages(package_data)

    # Distances: Stores all distances between addresses from file.
    distance_data = "C:\\Users\eddie\Desktop\C950 project\data\delivery_address_distances.csv"
    main_hub.add_distances(distance_data)

    # Addresses: Stores all address information from file.
    address_data = "C:\\Users\eddie\Desktop\C950 project\data\delivery_addresses.csv"
    main_hub.add_addresses(address_data)

    # Load Trucks & Set Hub Departure Time
    truck_1 = main_hub.truck_1
    truck_2 = main_hub.truck_2
    truck_3 = main_hub.truck_3

    # Truck 1 holds the packages that have to be delivered together (13,14,15,16,19,20)
    truck_1.add_packages([1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40], main_hub)
    truck_1.set_hub_departure_time(datetime.timedelta(hours=8))
    # Truck 2 is delayed until 10:20a because of unknown address of package 9
    truck_2.add_packages([3, 9, 12, 17, 18, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], main_hub)
    truck_2.set_hub_departure_time(datetime.timedelta(hours=10, minutes=20))
    # Truck 3 has to leave at 9:05a because of packages 6,25,28,32.
    truck_3.add_packages([2, 4, 5, 6, 7, 8, 10, 11, 25, 28, 32, 33], main_hub)
    truck_3.set_hub_departure_time(datetime.timedelta(hours=9, minutes=5))

    # Delivers Packages (Main Algorithm) - Finds nearest neighbor and delivers all packages for a specified truck
    package_delivery.deliver_packages(truck_1, main_hub)
    package_delivery.deliver_packages(truck_2, main_hub)
    package_delivery.deliver_packages(truck_3, main_hub)

    # Displays User Interface - Prompts users for a choice - Display total mileage or all package status at a specified time.
    user_interface.ui(main_hub)

if __name__ == '__main__':
    main()
