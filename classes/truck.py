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

    def set_hub_departure_time(self, time):
        self.hub_departure_time = time
        self.current_time = time
        for package in self.packages:
            package.set_hub_departure_time(time)

    def set_current_time(self, time):
        self.current_time = time


    ##### PACKAGES #####

    # Returns the number of packages on the truck
    def get_num_of_packages(self):
        return self.num_of_packages

    # Returns an array with all packages on the truck
    def get_packages(self):
        return self.packages

    def get_package(self,id):
        for package in self.packages:
            if package.id == str(id):
                return package

    # Adds packages hash to the truck
    # Stores an array of hash maps
    def add_package(self, package_to_add):
        if self.num_of_packages < self.max_packages:
            self.packages.append(package_to_add)
            self.num_of_packages += 1
        else:
            print(f'Truck #{self.truck_number} is fully loaded.')

    # Adds a list packages to the truck
    def add_packages(self, packages_to_add, hub):
        for package in packages_to_add:
            if self.num_of_packages < self.max_packages:
                new_package = hub.get_package(package)
                self.packages.append(new_package)
                self.num_of_packages += 1
            else:
                print(f'Truck #{self.truck_number} is fully loaded. Packages not loaded: {len(packages_to_add)-self.max_packages}')

    # Removes a package from the truck
    def remove_package(self):
        return

    ##### LOCATION #####


    ''' # Changes the current location of the truck 
    Update the current location of the truck and packages. 
    '''
    def set_location(self, location):
        self.current_location = location
        for package in self.packages:
            package.current_location = location

    # Display the current location of the truck
    def get_location(self):
        return self.current_location

    # Display the current trip's mileage
    def get_miles_traveled(self):
        print(f'Miles Traveled: {self.miles_traveled}')

    # Returns time traveled per trip: Time = distance/speed
    def calculate_time_traveled(self, distance):
        time = distance / self.speed
        return time

    def add_time_traveled(self, distance):
        time = self.calculate_time_traveled(distance)
        self.time_traveled+=time
        return self.time_traveled

    def get_time_traveled(self):
        minutes = (self.time_traveled % 1) * 60
        print(self.time_traveled)
        print(f'Time Traveled: {math.trunc(self.time_traveled)} hour(s) and {round(minutes)} minute(s).')

    # Update the current trip's mileage
    def update_miles_traveled(self):
        return

    def print_loaded_package(self):
        print(f'Truck Number: {self.truck_number}')
        for package in self.packages:
            package.print()
