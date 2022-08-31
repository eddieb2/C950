class Package:
    def __init__(self, package_id, address, deadline, city, zip_code, weight):
        self.id = package_id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zip = zip_code
        self.weight = weight
        self.tracking = {
            ''' status = en-route, delivered, or at hub
                {
                "11:00am": {"location": "xyz", "status": "at hub"}
                "12:00am": {"location": "xyz", "status": "en-route"},
                "1:00pm": {"location": "xyz", "status": "delivered"}
                }
            '''
        }

    # Returns tracking for a particular time
    def get_tracking(self):
        return

    # Update current tracking
    # Note: this will need to be updated for every minute in the day
    def update_tracking(self):
        return
