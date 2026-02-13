import os

# ===================== Base Class =====================
class Employee:
    """This is the main (parent) class for all employees."""

    def __init__(self, emp_id, name):
        # Private attributes (Encapsulation)
        self.__emp_id = emp_id
        self.__name = name

    def get_emp_id(self):
        return self.__emp_id

    def get_name(self):
        return self.__name

    # This will be overridden by subclasses (Abstraction)
    def calculate_pay(self):
        pass

    def display_details(self):
        print(f"Employee ID: {self.__emp_id}, Name: {self.__name}")


# ===================== Full-Time Employee =====================
class FullTimeEmployee(Employee):
    """Represents a full-time employee with a fixed monthly salary."""

    def __init__(self, emp_id, name, salary):
        super().__init__(emp_id, name)
        self.__salary = salary

    def calculate_pay(self):
        return self.__salary

    def update_salary(self, new_salary):
        if new_salary < 0:
            print("Salary cannot be negative.")
        else:
            self.__salary = new_salary
            print(" Salary updated successfully!")

    def display_details(self):
        super().display_details()
        print(f"Type: Full-Time | Monthly Salary: ${self.__salary:.2f}")


# ===================== Part-Time Employee =====================
class PartTimeEmployee(Employee):
    """Represents a part-time employee who is paid hourly."""

    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name)
        self.__hourly_rate = hourly_rate
        self.__hours_worked = hours_worked

    def calculate_pay(self):
        return self.__hourly_rate * self.__hours_worked

    def update_salary(self, hourly_rate=None, hours_worked=None):
        if hourly_rate is not None:
            if hourly_rate < 0:
                print("Hourly rate cannot be negative.")
                return
            self.__hourly_rate = hourly_rate

        if hours_worked is not None:
            if hours_worked < 0:
                print("Hours worked cannot be negative.")
                return
            self.__hours_worked = hours_worked

        print("Pay details updated successfully!")

    def display_details(self):
        super().display_details()
        print(f"Type: Part-Time | Hourly Rate: ${self.__hourly_rate:.2f}, Hours Worked: {self.__hours_worked}")


# ===================== File Handling =====================
def save_to_file(employees):
    """Saves all employee data to a text file."""
    with open("employees.txt", "w") as f:
        for emp in employees:
            if isinstance(emp, FullTimeEmployee):
                f.write(f"FullTime,{emp.get_emp_id()},{emp.get_name()},{emp.calculate_pay()}\n")
            elif isinstance(emp, PartTimeEmployee):
                f.write(f"PartTime,{emp.get_emp_id()},{emp.get_name()},{emp.calculate_pay()}\n")
    print("💾 Data saved successfully to employees.txt!")


def load_from_file():
    """Loads employee data from a text file."""
    employees = []
    if not os.path.exists("employees.txt"):
        return employees

    with open("employees.txt", "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 4:
                emp_type, emp_id, name, pay = parts
                pay = float(pay)
                if emp_type == "FullTime":
                    employees.append(FullTimeEmployee(emp_id, name, pay))
                elif emp_type == "PartTime":
                    # Default to 10 hours worked for simplicity
                    employees.append(PartTimeEmployee(emp_id, name, pay / 10, 10))
    print("Employees loaded successfully!")
    return employees


# ===================== Main Program =====================
def main():
    employees = load_from_file()

    while True:
        print("\n===== Employee Management System =====")
        print("1. Add Full-Time Employee")
        print("2. Add Part-Time Employee")
        print("3. View All Employees")
        print("4. Calculate Pay")
        print("5. Update Salary or Pay Info")
        print("6. Save and Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            # Add full-time employee
            name = input("Enter employee name: ")
            try:
                salary = float(input("Enter monthly salary: "))
                emp_id = str(len(employees) + 1)
                employees.append(FullTimeEmployee(emp_id, name, salary))
                print(" Full-time employee added successfully!")
            except ValueError:
                print("Please enter a valid number for salary.")

        elif choice == "2":
            # Add part-time employee
            name = input("Enter employee name: ")
            try:
                hourly_rate = float(input("Enter hourly rate: "))
                hours_worked = float(input("Enter hours worked: "))
                emp_id = str(len(employees) + 1)
                employees.append(PartTimeEmployee(emp_id, name, hourly_rate, hours_worked))
                print(" Part-time employee added successfully!")
            except ValueError:
                print("Please enter valid numbers for rate or hours.")

        elif choice == "3":
            # View all employees
            if not employees:
                print("📭 No employees found.")
            else:
                for emp in employees:
                    emp.display_details()
                    print("-" * 40)

        elif choice == "4":
            # Calculate pay
            emp_id = input("Enter employee ID: ")
            found = False
            for emp in employees:
                if emp.get_emp_id() == emp_id:
                    print(f"💰 {emp.get_name()} earns ${emp.calculate_pay():.2f} this month.")
                    found = True
                    break
            if not found:
                print("❌ Employee not found.")

        elif choice == "5":
            # Update pay info
            emp_id = input("Enter employee ID: ")
            found = False
            for emp in employees:
                if emp.get_emp_id() == emp_id:
                    found = True
                    if isinstance(emp, FullTimeEmployee):
                        try:
                            new_salary = float(input("Enter new salary: "))
                            emp.update_salary(new_salary)
                        except ValueError:
                            print("❌ Invalid number.")
                    else:
                        try:
                            new_rate = float(input("Enter new hourly rate: "))
                            new_hours = float(input("Enter new hours worked: "))
                            emp.update_salary(new_rate, new_hours)
                        except ValueError:
                            print("❌ Invalid number.")
                    break
            if not found:
                print("❌ Employee not found.")

        elif choice == "6":
            # Save and exit
            save_to_file(employees)
            print("👋 Exiting program. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Please enter a number between 1 and 6.")


main()