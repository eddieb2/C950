import operator
import datetime

# User Interface
def ui(hub):
    prompt = True

    while prompt:
        try:
            print("\n-------------------------------------------------")
            print("          WGUPS Package Delivery System          ")
            print("-------------------------------------------------\n")

            print("'P': View package statuses\n"
                  "'M': View total mileage\n"
                  "'X': Exit program\n")

            user_input = input("Enter choice: ")

            if user_input == 'X' or user_input == 'x':
                prompt = False
            elif user_input == 'P' or user_input == 'p':


                valid = True

                while valid:
                    print("\n'A': Check all packages\n'S': Check a specific package by ID ")
                    user_input_2 = input("\nEnter Choice: ")

                    if user_input_2 == 'A' or user_input_2 == 'a':
                        package_status_checker(hub, 1)
                        valid = False
                    elif user_input_2 == 'S' or user_input_2 == 's':
                        package_status_checker(hub, 0)
                        valid = False
                    elif user_input_2 == 'X' or user_input_2 == 'x':
                        prompt = False
                        return False

            elif user_input == 'M' or user_input == 'm':
                truck_mileage_display(hub)
        except:
            print("Error")


# Displays all package statuses at a given time
def package_status_checker(hub, flag):
    print("\n----------------------")
    print("Package Status Checker")
    print("----------------------\n")

    print("Enter a military time below to view all package statuses. \n")

    prompt = True

    while prompt:
        hour = None
        minute = None
        input_package_id = None
        packages_array = hub.storage.lookup_all()
        packages_array.sort(key=operator.attrgetter('id'))  # sorts by class id

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

        if flag == 0:
            while input_package_id == None:
                try:
                    input_package_id = int(input("Enter package id: "))

                    val = hub.storage.lookup(str(input_package_id))

                    if val == None:
                        input_package_id = None
                        print("Invalid ID!.")


                except:
                    print("Error")

        print("\n------------------------------")
        print(f"Package Information at {datetime.timedelta(hours=hour, minutes=minute)}")
        print("------------------------------\n")

        if flag == 1:  # prints all packages and information
            for package in packages_array:
                status = package.calculate_status(datetime.timedelta(hours=int(hour), minutes=int(minute)))
                if status == 'DELIVERED':
                    print(f'Package ID: {str(package.id):20s} Status: {status} at {str(package.time_delivered):20s} Address: {package.street}')
                else:
                    print(f'Package ID: {str(package.id):20s} Status: {status:33s} Address: {package.street}')
        elif flag == 0:  # prints one package and it's information
            for package in packages_array:
                if package.id == input_package_id:
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
    print(f'Total Mileage: {round(hub.calculate_all_trucks_mileage(), 2)} mi.')
