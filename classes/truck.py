class Truck:
    def __init__(self, truck_number):
        self.truck_number = truck_number
        self.current_location = None # default should be the HUB
        self.miles_traveled = 0
        self.packages = []
        self.num_of_packages = 0
        self.max_packages = 16

    ##### PACKAGES #####

    # Returns the number of packages on the truck
    def get_num_of_packages(self):
        return self.num_of_packages

    # Returns an array with all packages on the truck
    def get_packages(self):
        return self.packages

    # Adds a package to the truck
    def set_package(self, package_to_add):
        if self.num_of_packages < self.max_packages:
            self.packages.append(package_to_add)
            self.num_of_packages += 1
        else:
            print(f'Truck #{self.truck_number} is fully loaded.')

    # Adds packages to the truck
    def set_packages(self, packages_to_add):
        for package in packages_to_add:
            if self.num_of_packages < self.max_packages:
                self.packages.append(package)
                self.num_of_packages += 1
            else:
                print(f'Truck #{self.truck_number} is fully loaded.')

    # Removes a package from the truck
    def remove_package(self):
        return

    ##### LOCATION #####

    # Changes the current location of the truck
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
