import operator
import datetime

# User Interface
def ui(hub):
    prompt = True

    while prompt:
        print("\n-------------------------------------------------")
        print("          WGUPS Package Delivery System          ")
        print("-------------------------------------------------\n")

        user_input = input("Enter P to view package statues\n"
              "Enter M to view total mileage\n"
              "Enter X to exit: ")

        if user_input == 'X' or user_input == 'x':
            prompt = False
        elif user_input == 'P' or user_input == 'p':
            package_status_checker(hub)
        elif user_input == 'M' or user_input == 'm':
            truck_mileage_display(hub)

# Displays all package statuses at a given time
def package_status_checker(hub):
    print("\n----------------------")
    print("Package Status Checker")
    print("----------------------\n")

    print("Enter a military time below to view all package statuses. \n")

    prompt = True

    while prompt:
        hour = None
        minute = None


        while hour == None:
            try:
                hour = int(input("Enter hour: "))
            except:
                print("Invalid Hour!")
        while minute == None:
            try:
                minute = int(input("Enter minutes: "))
            except:
                print("Invalid Minutes!")

        print("\n------------------------------")
        print(f"Package Information at {datetime.timedelta(hours=hour, minutes=minute)}")
        print("------------------------------\n")

        packages_array = hub.storage.lookup_all()
        packages_array.sort(key=operator.attrgetter('id'))  # sorts by class id

        for package in packages_array:
            status = package.calculate_status(datetime.timedelta(hours=int(hour), minutes=int(minute)))
            if status == 'DELIVERED':
                print(f'Package ID: {str(package.id):20s} Status: {status} at {str(package.time_delivered):20s} Address: {package.street}')
            else:
                print(f'Package ID: {str(package.id):20s} Status: {status:33s} Address: {package.street}')

        prompt = False

# Displays total truck mileage
def truck_mileage_display(hub):
    print("\n------------------------")
    print("Truck Mileage Information")
    print("-------------------------\n")

    print(f'Truck #1: {hub.truck_1.miles_traveled} mi.')
    print(f'Truck #2: {hub.truck_2.miles_traveled} mi.')
    print(f'Truck #3: {hub.truck_3.miles_traveled} mi.')
    print(f'Total Mileage: {round(hub.calculate_all_trucks_mileage(),2)} mi.')
