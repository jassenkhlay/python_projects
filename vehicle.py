import os

# ---------------- Base Class ----------------
class Vehicle:
    def __init__(self, vehicle_no, rent_per_day, available=True):
        self.__vehicle_no = vehicle_no
        self.__rent_per_day = rent_per_day
        self.__available = available

    def get_vehicle_no(self):
        return self.__vehicle_no

    def is_available(self):
        return self.__available

    def set_available(self, status):
        self.__available = status

    def get_rent_per_day(self):
        return self.__rent_per_day

    # Abstract method placeholder
    def calculate_rent(self, days):
        raise NotImplementedError("Subclasses must implement calculate_rent method.")

    def rent_vehicle(self):
        if self.__available:
            self.__available = False
            print(f"Vehicle {self.__vehicle_no} has been rented.")
        else:
            print(f"Vehicle {self.__vehicle_no} is not available for rent.")

    def return_vehicle(self, days):
        if not self.__available:
            self.__available = True
            rent = self.calculate_rent(days)
            print(f"Vehicle {self.__vehicle_no} returned. Total rent: ₹{rent}")
            return rent
        else:
            print(f"Vehicle {self.__vehicle_no} was not rented.")
            return 0

    def __str__(self):
        status = "Available" if self.__available else "Rented"
        return f"{self.__class__.__name__} | No: {self.__vehicle_no} | ₹{self.__rent_per_day}/day | {status}"


# ---------------- Derived Classes ----------------
class Car(Vehicle):
    def calculate_rent(self, days):
        return self.get_rent_per_day() * days

class Bike(Vehicle):
    def calculate_rent(self, days):
        # 10% discount for bikes rented more than 5 days
        rent = self.get_rent_per_day() * days
        if days > 5:
            rent *= 0.9
        return rent

class Truck(Vehicle):
    def calculate_rent(self, days):
        # 20% extra charge for heavy trucks
        return self.get_rent_per_day() * days * 1.2


# ---------------- File Handling ----------------
def load_vehicles():
    vehicles = []
    if os.path.exists("vehicles.txt"):
        with open("vehicles.txt", "r") as f:
            for line in f:
                data = line.strip().split(",")
                if len(data) == 4:
                    vtype, vno, rent, status = data
                    rent = float(rent)
                    available = status == "True"
                    if vtype == "Car":
                        vehicles.append(Car(vno, rent, available))
                    elif vtype == "Bike":
                        vehicles.append(Bike(vno, rent, available))
                    elif vtype == "Truck":
                        vehicles.append(Truck(vno, rent, available))
    return vehicles


def save_vehicles(vehicles):
    with open("vehicles.txt", "w") as f:
        for v in vehicles:
            f.write(f"{v.__class__.__name__},{v.get_vehicle_no()},{v.get_rent_per_day()},{v.is_available()}\n")


# ---------------- Menu Functions ----------------
def add_vehicle(vehicles):
    vtype = input("Enter vehicle type (Car/Bike/Truck): ").capitalize()
    vno = input("Enter vehicle number: ")
    try:
        rent = float(input("Enter rent per day: "))
    except ValueError:
        print("Invalid rent amount!")
        return

    if vtype == "Car":
        v = Car(vno, rent)
    elif vtype == "Bike":
        v = Bike(vno, rent)
    elif vtype == "Truck":
        v = Truck(vno, rent)
    else:
        print("Invalid vehicle type!")
        return

    vehicles.append(v)
    save_vehicles(vehicles)
    print(f"{vtype} {vno} added successfully.")


def rent_vehicle(vehicles):
    vno = input("Enter vehicle number to rent: ")
    for v in vehicles:
        if v.get_vehicle_no() == vno:
            v.rent_vehicle()
            save_vehicles(vehicles)
            return
    print("Vehicle not found!")


def return_vehicle(vehicles):
    vno = input("Enter vehicle number to return: ")
    for v in vehicles:
        if v.get_vehicle_no() == vno:
            try:
                days = int(input("Enter number of days rented: "))
                if days <= 0:
                    raise ValueError
            except ValueError:
                print("Invalid number of days!")
                return
            v.return_vehicle(days)
            save_vehicles(vehicles)
            return
    print("Vehicle not found!")


def display_vehicles(vehicles, available=True):
    print("\nAvailable Vehicles:" if available else "\nRented Vehicles:")
    for v in vehicles:
        if v.is_available() == available:
            print(v)
    print("-" * 40)


# ---------------- Main Program ----------------
def main():
    vehicles = load_vehicles()

    while True:
        print("\n=== Vehicle Rental System ===")
        print("1. Add Vehicle")
        print("2. Rent Vehicle")
        print("3. Return Vehicle")
        print("4. Show Available Vehicles")
        print("5. Show Rented Vehicles")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_vehicle(vehicles)
        elif choice == "2":
            rent_vehicle(vehicles)
        elif choice == "3":
            return_vehicle(vehicles)
        elif choice == "4":
            display_vehicles(vehicles, available=True)
        elif choice == "5":
            display_vehicles(vehicles, available=False)
        elif choice == "6":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice! Please try again.")



main()