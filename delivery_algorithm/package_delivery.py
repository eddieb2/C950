import datetime

# Nearest Neighbor Algorithm --- Returns the nearest neighbor from the current location, the distance from the current location to the nearest neighbor,
# and the package to be removed when the nearest neighbor is reached.
# Time Complexity: O(n)
# Space Complexity: O(1)
def find_nearest_neighbor(truck, hub):
    nearest_address = None
    distance = None
    package_to_remove = None

    # Iterate through the trucks packages and find the package with the closest address to the truck's current location
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

# Deliver Packages --- Finds the nearest neighbor, updates all information related to time, distance and location, and removes the package from storage
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def deliver_packages(truck, hub):

    while len(truck.packages) > 0:
        nearest_info = find_nearest_neighbor(truck, hub) # calculate the nearest neighbor from the current location for a specified truck and hub

        nearest_address = nearest_info[0]
        distance = nearest_info[1]
        package_to_deliver = nearest_info[2]
        time_traveled = truck.calculate_time_traveled(distance)

        truck.set_current_time(truck.current_time + datetime.timedelta(hours=time_traveled)) # updates truck current time
        truck.update_miles_traveled(distance) # increments total miles traveled
        truck.add_time_traveled(distance) # increments total time traveled
        package_to_deliver.set_time_delivered(truck.current_time) # update the time the package was delivered
        truck.packages.remove(package_to_deliver) # removes the delivered package
        truck.current_location = nearest_address # changes current location to the location where the package was delivered
