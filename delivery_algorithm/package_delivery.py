import datetime

# Nearest Neighbor Algorithm with delivery time prioritization (self-adjusting algorithm)
#
# This algorithm prioritizes picking packages with specific time deadlines first. If the algorithm finds a "priority" package, it will then check if that
# package is the closest in relation to the truck, against all other priority packages with the same deadline. If there are no priority packages,
# the algorithm delivers strictly based on which neighbor is nearest.
#
# Returns the nearest neighbor from the current location, the distance from the current location to the nearest neighbor,
# and the package to be removed when the nearest neighbor is reached.

# Time Complexity: O(n)
# Space Complexity: O(1)
def find_nearest_neighbor(truck, hub):
    nearest_address = None
    distance = None
    package_to_remove = None

    is_priority_package = False
    priority_package = None
    priority_package_deadline = None
    priority_package_distance = None

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Check if there are any priority packages - if a priority package is found -> find the package with the soonest deadline and closest distance -> return it
    for package in truck.packages: # Time Complexity: O(n)
        if package.deadline != 'EOD':
            is_priority_package = True

            # Convert deadline string into a usable timedelta
            hour = int(package.deadline[0:2])
            minute = int(package.deadline[3:5])
            cur_package_deadline = datetime.timedelta(hours=hour, minutes=minute)

            cur_package = package
            cur_package_distance = hub.get_distance_between(truck.current_location, package.street) # Time Complexity: O(1)

            # is there a currently a priority package ?
            # is the deadline of the current package sooner than the previous priority package?
                # assign a new priority package, deadline, and distance
            if priority_package is None or priority_package_deadline > cur_package_deadline:
                priority_package = cur_package
                priority_package_deadline = cur_package_deadline
                priority_package_distance = cur_package_distance

            # is the previous priority package's deadline equal to the current package's deadline?
                # which package address is closer to the truck?
                    # Assign the closest package information to priority package, deadline, and distance
            elif priority_package_deadline == cur_package_deadline:
                if priority_package_distance > cur_package_distance:
                    priority_package = cur_package
                    priority_package_deadline = cur_package_deadline
                    priority_package_distance = cur_package_distance


    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # Iterate through the truck's non-priority packages and find the package with the closest address to the truck's current location
    if is_priority_package == False:
        for index, package in enumerate(truck.packages): # Time Complexity: O(n)
            # for the first iteration, set nearest address, distance, and package to remove so that the follow iteration has something to compare itself against
            if index == 0:
                nearest_address = package.street
                distance = hub.get_distance_between(truck.current_location, nearest_address) # Time Complexity: O(1)
                package_to_remove = package
            else:
                # calculate distances between current nearest address/truck and the next address/truck
                dist1 = hub.get_distance_between(truck.current_location, nearest_address) # Time Complexity: O(1)
                dist2 = hub.get_distance_between(truck.current_location, package.street) # Time Complexity: O(1)

                # if the previous nearest neighbor (nearest_address) is further than the distance between the current location and the next neighbor,
                # change nearest_address to the next neighbor (package.street)
                if dist1 > dist2:
                    nearest_address = package.street
                    distance = dist2
                    package_to_remove = package

        return [nearest_address, distance, package_to_remove]

    return [priority_package.street, priority_package_distance, priority_package]

# Deliver Packages --- Finds the nearest neighbor, updates all information related to time, distance and location, and removes the package from storage
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def deliver_packages(truck, hub):

    while len(truck.packages) > 0: # O(n)
        nearest_info = find_nearest_neighbor(truck, hub) # calculate the nearest neighbor from the current location for a specified truck and hub - O(n)

        nearest_address = nearest_info[0]
        distance = nearest_info[1]
        package_to_deliver = nearest_info[2]
        time_traveled = truck.calculate_time_traveled(distance) # Time Complexity: O(1)

        truck.set_current_time(truck.current_time + datetime.timedelta(hours=time_traveled)) # updates truck current time - Time Complexity: O(1)
        truck.update_miles_traveled(distance) # increments total miles traveled - Time Complexity: O(1)
        truck.add_time_traveled(distance) # increments total time traveled - Time Complexity: O(1)
        package_to_deliver.set_time_delivered(truck.current_time) # update the time the package was delivered - Time Complexity: O(1)
        truck.packages.remove(package_to_deliver) # removes the delivered package - Time Complexity: O(n)
        truck.current_location = nearest_address # changes current location to the location where the package was delivered - Time Complexity: O(1)
