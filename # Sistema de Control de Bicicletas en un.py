# Bicycle Shop Control System
# Object-Oriented Programming - Encapsulation

class BicycleWorkshop:

    def __init__(self, serial, cost_per_hour):
        self._serial = serial
        self._entry_time = None
        self._exit_time = None
        self._cost_per_hour = cost_per_hour

    # Saves the time when the bicycle arrives
    def register_entry(self, time):
        self._entry_time = time

    # Saves the time when the bicycle is picked up
    def register_exit(self, time):
        if time <= self._entry_time:
            print("Exit time must be greater than entry time.")
            return False

        self._exit_time = time
        return True

    # Calculates the total cost based on the time the bicycle stayed
    def calculate_total(self, exit_time):
        if exit_time <= self._entry_time:
            print("Exit time must be greater than entry time.")
            return None

        hours = exit_time - self._entry_time
        total = hours * self._cost_per_hour
        return total

    def get_serial(self):
        return self._serial


# List where all registered bicycles are stored
bicycles = []


def register_bicycle():
    serial = input("Bicycle serial number: ")
    entry_time = float(input("Entry time: "))
    cost = float(input("Cost per hour: "))

    bicycle = BicycleWorkshop(serial, cost)
    bicycle.register_entry(entry_time)
    bicycles.append(bicycle)

    print("Bicycle registered successfully.")


def find_bicycle(serial):
    for bicycle in bicycles:
        if bicycle.get_serial() == serial:
            return bicycle

    return None


def register_exit():
    serial = input("Serial number of the bicycle leaving: ")
    bicycle = find_bicycle(serial)

    if bicycle is None:
        print("There is no bicycle with that serial number.")
        return

    exit_time = float(input("Exit time: "))

    if bicycle.register_exit(exit_time):
        total = bicycle.calculate_total(exit_time)
        print("Total amount to pay:", total)


def show_bicycles():
    if len(bicycles) == 0:
        print("No bicycles registered.")

    for bicycle in bicycles:
        print("Serial number:", bicycle.get_serial())


# Main program menu
option = 0

while option != 4:

    print("\n1. Register bicycle entry")
    print("2. Register bicycle exit and calculate cost")
    print("3. View registered bicycles")
    print("4. Exit")

    option = int(input("Choose an option: "))

    if option == 1:
        register_bicycle()

    elif option == 2:
        register_exit()

    elif option == 3:
        show_bicycles()

    elif option == 4:
        print("End of program.")

    else:
        print("Invalid option.")
