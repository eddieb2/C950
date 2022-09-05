from classes.hash_table import HashTable
from classes.package import Package
from classes.truck import Truck
import csv

class Hub:
    def __init__(self):
        self.storage = HashTable()
        self.package_log = HashTable()
        self.truck_1 = Truck(1)
        self.truck_2 = Truck(2)

    def get_package(self, id):
        return self.storage.lookup(id)

    # Adds packages to storage
    def add_packages(self, file_path):
        # read the package data file
        with open(file_path) as package_file:
            package_data = csv.reader(package_file, delimiter=",",
                                      quotechar='"')
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

    # check truck package logs if any updates and update the master log
    def update_package_log(self):
        return

    # Transfers packages to trucks from storage
    def transfer_packages_to_truck(self, package_key, truck_number):
        # add to truck by using Truck methods
        self.storage.delete(package_key)

    # Prints all packages in storage
    def print_packages(self):
        self.storage.print()
