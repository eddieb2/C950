import math
class Truck:
    def __init__(self, truck_number):
        self.truck_number = truck_number
        self.current_location = "4001 South 700 East" # default = hub
        self.current_time = None
        self.hub_departure_time = None
        self.miles_traveled = 0
        self.time_traveled = 0
        self.packages = []
        self.num_of_packages = 0
        self.max_packages = 16
        self.speed = 18

    ################
    # Time Methods #
    ################

    # Sets the hub departure time - Time Complexity - Worst: O(n)
    def set_hub_departure_time(self, time):
        self.hub_departure_time = time
        self.current_time = time
        for package in self.packages:
            package.set_hub_departure_time(time)

    # Sets the current time - Time Complexity - Worst: O(1)
    def set_current_time(self, time):
        self.current_time = time

    # Returns current time of the truck - Time Complexity - Worst: O(1)
    def get_current_time(self):
        return self.current_time

    # Returns time traveled per trip - Time Complexity - Worst: O(1)
    def calculate_time_traveled(self, distance):
        time = distance / self.speed
        return time

    # Increments the time traveled - Time Complexity - Worst: O(1)
    def add_time_traveled(self, distance):
        time = self.calculate_time_traveled(distance)
        self.time_traveled+=time
        return self.time_traveled

    # Returns the current time traveled - Time Complexity - Worst: O(1)
    def get_time_traveled(self):
        minutes = (self.time_traveled % 1) * 60
        print(self.time_traveled)
        print(f'Time Traveled: {math.trunc(self.time_traveled)} hour(s) and {round(minutes)} minute(s).')

    ###################
    # Package Methods #
    ###################

    # Returns the number of packages on the truck - Time Complexity - Worst: O(1)
    def get_num_of_packages(self):
        return self.num_of_packages

    # Returns an array with all packages on the truck - Time Complexity - Worst: O(1)
    def get_packages(self):
        return self.packages

    # Returns a package by id - Time Complexity - Worst: O(n)
    def get_package(self,id):
        for package in self.packages:
            if package.id == str(id):
                return package

    # Adds a package to the truck - Time Complexity - Worst: O(1)
    def add_package(self, package_to_add):
        if self.num_of_packages < self.max_packages:
            self.packages.append(package_to_add)
            self.num_of_packages += 1
        else:
            print(f'Truck #{self.truck_number} is fully loaded.')

    # Adds a list of packages to the truck - Time Complexity - Worst: O(1)
    def add_packages(self, packages_to_add, hub):
        for package in packages_to_add:
            if self.num_of_packages < self.max_packages:
                new_package = hub.get_package(package)
                self.packages.append(new_package)
                self.num_of_packages += 1
            else:
                print(f'Truck #{self.truck_number} is fully loaded. Packages not loaded: {len(packages_to_add)-self.max_packages}')


    ####################
    # Location Methods #
    ####################

    # Display the current location of the truck - Time Complexity - Worst: O(1)
    def get_location(self):
        return self.current_location

    # Updates the current location of the truck and its loaded packages - Time Complexity - Worst: O(n)
    def set_location(self, location):
        self.current_location = location
        for package in self.packages:
            package.current_location = location

    ###################
    # Mileage Methods #
    ###################

    # Returns the current amount of miles traveled - Time Complexity - Worst: O(1)
    def get_miles_traveled(self):
        return self.miles_traveled

    # Update the current trip's mileage - Time Complexity - Worst: O(1)
    def update_miles_traveled(self, distance):
        self.miles_traveled += distance

    #################
    # Print Methods #
    #################

    # Prints all loaded packages - Time Complexity - Worst: O(n)
    def print_loaded_package(self):
        print(f'Truck Number: {self.truck_number}')
        for package in self.packages:
            package.print()
