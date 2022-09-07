from classes.hash_table import HashTable
from classes.status_location import StatusLocation
import datetime
class Package:
    def __init__(self, package_id, street, city, state, zip, deadline,
                 weight, special_notes):
        self.id = int(package_id)
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.special_notes = special_notes
        self.hub_departure_time = None
        self.time_delivered = None

        # Status
        ''' status = en-route, delivered, or at hub
        '''

    # Returns a status for a particular time
    def calculate_status(self, time):
        if time >= self.time_delivered:
            return StatusLocation(2).name
        elif time >= self.hub_departure_time:
            return StatusLocation(1).name
        else:
            return StatusLocation(0).name

    # Sets the time delivered for status purposes
    def set_time_delivered(self, time):
        self.time_delivered = time

    def set_hub_departure_time(self, time):
        self.hub_departure_time = time

    # Print
    def print(self):
        print([self.id,self.street,self.state,self.zip,self.deadline,
               self.weight,self.special_notes,self.hub_departure_time,self.time_delivered])


    def print_times(self):
        print([self.hub_departure_time, self.time_left_hub])