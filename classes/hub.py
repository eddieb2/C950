from classes.hash_table import HashTable
from classes.package import Package
from classes.truck import Truck
import csv

class Hub:
    def __init__(self):
        self.storage = HashTable()
        self.storage_size = 0
        self.distances = []
        self.addresses = HashTable()
        self.truck_1 = Truck(1)
        self.truck_2 = Truck(2)
        self.truck_3 = Truck(3)
        self.garage = [self.truck_1, self.truck_2, self.truck_3]

    ####################
    # Distance Methods #
    ####################

    # Returns an 2-dimensional array of distances - Time Complexity - Worst: O(1)
    def get_distances(self):
        return self.distances

    # Returns the distance between two addresses - Time Complexity - Worst: O(1)
    def get_distance_between(self, full_street_address_1, full_street_address_2):
        location_1 = self._get_address_matrix_number(full_street_address_1)
        location_2 = self._get_address_matrix_number(full_street_address_2)
        return float(self.distances[location_1][location_2])

    # Reads distance data from file and stores the data in the distance array
    def add_distances(self, file_path):  # Time Complexity - Worst: O(n)
        # Read the distances file
        with open(f"{file_path}") as distance_file:
            distance_data = csv.reader(distance_file, delimiter=",", quotechar='"')
            # Add the data to the distances array
            for distance in distance_data:
                self.distances.append(distance)

    ###################
    # Address Methods #
    ###################

    # Returns the address number id (0-27) -- used for locating the address in the distance table - Time Complexity - Worst: O(1)
    def _get_address_matrix_number(self, full_street_address):
        return int(self.addresses.lookup(full_street_address))


    # Reads address data from a file and stores the data in the address array - Time Complexity - Worst: O(n)
    def add_addresses(self, file_path):
        # Read the address data file
        with open(f"{file_path}") as address_file:
            address_data = csv.reader(address_file, delimiter=",", quotechar='"')
            # Add data to the addresses array
            for address in address_data:
                # key = street, value = addressID - used for O(1) lookup in _get_address_matrix_number()
                self.addresses.insert(address[2], address[0])

    ###################
    # Package Methods #
    ###################

    # Returns a package from storage - Time Complexity - Worst: O(1)
    def get_package(self, id):
        return self.storage.lookup(str(id))

    # Reads package data from a file, creates a Package, and adds it to storage - Time Complexity - Worst: O(n)
    def add_packages(self, file_path):
        # Read the package data file
        with open(f"{file_path}") as package_file:
            package_data = csv.reader(package_file, delimiter=",", quotechar='"')
            for package in package_data:
                # Create a new Package
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

    #########################
    # Total Mileage Methods #
    #########################

    # Returns the total mileage for all trucks - Time Complexity - Worst: O(n)
    def calculate_all_trucks_mileage(self):
        total_mileage = 0
        for truck in self.garage:
            total_mileage+=truck.miles_traveled
        return total_mileage

    #################
    # Print Methods #
    #################

    # Prints all packages in storage Time Complexity - Worst: O(n)
    def print_packages(self):
        self.storage.print()

    # Prints all distances between addresses - Time Complexity - Worst: O(n)
    def print_distances(self):
        for distance in self.distances:
            print(distance)
