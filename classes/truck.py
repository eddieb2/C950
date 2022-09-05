class Truck:
    def __init__(self, truck_number):
        self.truck_number = truck_number
        self.current_location = "4001 South 700 East" # default = hub
        self.current_time = None
        self.miles_traveled = 0
        self.packages = []
        self.num_of_packages = 0
        self.max_packages = 16 # might not be needed
        self.speed = 18 # max speed

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
    Update the current location/time of the truck and packages. 
    '''
    def set_location(self, location):
        self.current_location = location

    # Display the current location of the truck
    def get_location(self):
        return self.current_location

    # Display the current trip's mileage
    def get_miles_traveled(self):
        return

    # Update the current trip's mileage
    def update_miles_traveled(self):
        return

    def print_loaded_package(self):
        print(f'Truck Number: {self.truck_number}')
        for package in self.packages:
            package.print()
