from classes.hash_table import HashTable
from classes.package import Package
from classes.truck import Truck
import csv

class Hub:
    def __init__(self):
        self.storage = HashTable()
        self.storage_size = 0
        self.distances = []
        self.addresses = []

        self.truck_1 = Truck(1)
        self.truck_2 = Truck(2)
        self.truck_3 = Truck(3)

        self.garage = [self.truck_1, self.truck_2, self.truck_3]

    # Returns a package
    def get_package(self, id):
        return self.storage.lookup(str(id))

    # Returns an 2-dimensional array of distances
    def get_distances(self):
        return self.distances

    # Returns the distance between two locations
    # takes strings (full address) and returns a float (distance)
    def get_distance_between(self, full_street_address_1, full_street_address_2):
        location_1 = self._get_address_matrix_number(full_street_address_1)
        location_2 = self._get_address_matrix_number(full_street_address_2)
        return float(self.distances[location_1][location_2])

    # Returns the address number id (0-27) -- used for locating the address in the distance table
    def _get_address_matrix_number(self, full_street_address):
        for address in self.addresses:
            if address[2] == full_street_address:
                return int(address[0])


    # Stores addresses
    def add_addresses(self, file_path):
        with open(file_path) as address_file:
            address_data = csv.reader(address_file, delimiter=",", quotechar='"')
            for address in address_data:
                self.addresses.append(address)

    # Stores distances
    def add_distances(self, file_path):
        with open(file_path) as distance_file:
            distance_data = csv.reader(distance_file, delimiter=",", quotechar='"')
            for distance in distance_data:
                self.distances.append(distance)

    # Adds packages to storage
    def add_packages(self, file_path):
        # read the package data file
        with open(file_path) as package_file:
            package_data = csv.reader(package_file, delimiter=",", quotechar='"')
            for package in package_data:
                # create a new Package
                id = package[0]
                street = package[1]
                city = package[2]
                state = package[3]
                zip = package[4]
                dead_line = package[5]
                weight = package[6]
                special_notes = package[7]

                new_package = Package(id, street, city, state, zip, dead_line, weight, special_notes)

                # Insert the new package
                self.storage.insert(id, new_package)
                self.storage_size+=1


    # Prints all packages in storage
    def print_packages(self):
        self.storage.print()

    # Prints all distances between addresses
    def print_distances(self):
        for distance in self.distances:
            print(distance)

    # Prints all address information
    def print_addresses(self):
        for address in self.addresses:
            print(address)

    def calculate_all_trucks_mileage(self):
        total_mileage = 0
        for truck in self.garage:
            total_mileage+=truck.miles_traveled
        return total_mileage