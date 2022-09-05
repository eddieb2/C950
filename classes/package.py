from classes.hash_table import HashTable
from classes.status_location import StatusLocation
class Package:
    def __init__(self, package_id, street, city, state, zip, deadline,
                 weight, special_notes):
        self.id = package_id
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.special_notes = special_notes
        self.status = StatusLocation(0)

        # Status
        ''' status = en-route, delivered, or at hub
        '''


    # Returns tracking for a particular time
    def get_status(self):
        return self.status.name

    # Update current status
    def update_status(self, status):
        self.status = StatusLocation(status)

    # Print
    def print(self):
        print([self.id,self.street,self.state,self.zip,self.deadline,
               self.weight,self.special_notes,self.status.name])
