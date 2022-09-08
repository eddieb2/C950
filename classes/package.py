from classes.status_location import StatusLocation
class Package:
    def __init__(self, package_id, street, city, state, zip, deadline,
                 weight, special_notes):
        self.id = int(package_id)
        self.street = street # "address"
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.special_notes = special_notes
        self.hub_departure_time = None
        self.time_delivered = None
        self.status = StatusLocation(0)


    ##################
    # Status Methods #
    ##################

    # Returns a status for a particular time
    def calculate_status(self, time):
        if time >= self.time_delivered:
            self.status = StatusLocation(2)
            return StatusLocation(2).name
        elif time >= self.hub_departure_time:
            self.status = StatusLocation(1)
            return StatusLocation(1).name
        else:
            self.status = StatusLocation(0)
            return StatusLocation(0).name

    ################
    # Time Methods #
    ################

    # Sets the time that the package was delivered
    def set_time_delivered(self, time):
        self.time_delivered = time

    # Sets the time that a package departed the hub
    def set_hub_departure_time(self, time):
        self.hub_departure_time = time

    #################
    # Print Methods #
    #################

    def print(self):
        print([self.id,self.street,self.state,self.zip,self.deadline,
               self.weight,self.special_notes,self.hub_departure_time,self.time_delivered])

    def print_times(self):
        print([self.hub_departure_time, self.hub_departure_time])