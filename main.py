from classes.status_location import  StatusLocation
from classes.hub import Hub

# Return the address and distance
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

# Deliver Packages
def deliver_packages(truck, hub):

    while len(truck.packages) > 0:
        nearest_info = find_nearest_neighbor(truck, hub)
        print(nearest_info[0],nearest_info[1])
        truck.miles_traveled += nearest_info[1]
        truck.packages.remove(nearest_info[2])
        truck.current_location = nearest_info[0]

    print(truck.miles_traveled)

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

    # Load Trucks
    truck_1 = main_hub.truck_1
    truck_2 = main_hub.truck_2
    truck_3 = main_hub.truck_3

    truck_1.add_packages([], main_hub) #
    truck_2.add_packages([3,18,36,38], main_hub) #
    truck_3.add_packages([], main_hub) #

    # 3,18,36,38 have to be on truck 2
    # 13,14,15,16,19,20 have to be together

    # print(find_nearest_neighbor(truck_1,main_hub))
    # deliver_packages(truck_1, main_hub)
    # deliver_packages(truck_2, main_hub)
    # deliver_packages(truck_3, main_hub)
    # print(truck_1.miles_traveled + truck_2.miles_traveled + truck_3.miles_traveled)
    print(main_hub.storage_size)

if __name__ == '__main__':
    main()



    '''
    1.9
    2.0
    '''

