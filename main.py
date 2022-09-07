# Edward Andrew Blanciak #001518541
from classes.hub import Hub
import datetime
from CLI import user_interface

# Return the address and distance  - O(n)
def find_nearest_neighbor(truck, hub):
    nearest_address = None
    distance = None
    package_to_remove = None

    # Loop through the trucks packages and find the package with the closest address to the truck's current location
    for index, package in enumerate(truck.packages):
        if index == 0:
            nearest_address = package.street
            distance = hub.get_distance_between(truck.current_location, nearest_address)
            package_to_remove = package
        else:
            dist1 = hub.get_distance_between(truck.current_location, nearest_address)
            dist2 = hub.get_distance_between(truck.current_location, package.street)

            if dist1 > dist2:
                nearest_address = package.street
                distance = dist2
                package_to_remove = package

    return [nearest_address, distance, package_to_remove]

# Deliver Packages - O(n^2)
def deliver_packages(truck, hub):

    while len(truck.packages) > 0:
        nearest_info = find_nearest_neighbor(truck, hub)
        nearest_address = nearest_info[0]
        distance = nearest_info[1]
        package_to_deliver = nearest_info[2]
        time_traveled = truck.calculate_time_traveled(distance)

        truck.set_current_time(truck.current_time + datetime.timedelta(hours=time_traveled))
        truck.miles_traveled += distance # increments total miles traveled
        truck.add_time_traveled(distance) # increments total time traveled
        package_to_deliver.set_time_delivered(truck.current_time) # update the time the package was delivered
        truck.packages.remove(package_to_deliver) # removes the delivered package
        truck.current_location = nearest_address # changes current location to the location where the package was delivered



def main():
    # Hub Creation: Creates a hub where the packages will be stored.
    main_hub = Hub()

    # Packages: Creates and stores packages from file.
    package_data = "C:\\Users\eddie\Desktop\C950 project\data\package_data.csv"
    main_hub.add_packages(package_data)

    # Distances: Stores all distances between addresses.
    distance_data = "C:\\Users\eddie\Desktop\C950 project\data\delivery_address_distances.csv"
    main_hub.add_distances(distance_data)

    # Addresses: Stores all address information.
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
    truck_3.set_hub_departure_time(datetime.timedelta(hours=9, minutes=5)
)

    # Deliver Packages
    deliver_packages(truck_1, main_hub)
    deliver_packages(truck_2, main_hub)
    deliver_packages(truck_3, main_hub)

    user_interface.ui(main_hub)

if __name__ == '__main__':
    main()



    '''
NOTES FOR 9/6

finish up loading trucks with proper packages (manually is simple)
figure out how to track the time to deliver packages - calc mph 
implement feature to calculate where a package is at a specific time
implement cli prompt to show package times
update comments
finish project document and submit
    '''

''' Package notes
    # [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40] (#15 needs to be delivered first)
    # [3, 12, 17, 18, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39]
    # [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33] - Leaves at 9:05am (#6)

    # 13,14,15,16,19,20 - have to be together
    # 3,18,36,38 - have to be on truck 2
    # 6,25,28,32 cant leave until 9:05
    # 9 cant be delievered until 1020
'''