from Employee import Employee
from EmployeesManager import EmployeesManager


class Manager:
    def __init__(self):
        self.manager = EmployeesManager()
        self.logged_in = False

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == "admin" and password == "admin":
            print("Login successful!")
            self.logged_in = True
        else:
            print("Invalid credentials. Try again.")

    def show_menu(self):
        print("1. Add Employee")
        print("2. Show All Employees")
        print("3. Remove Employees by Age Range")
        print("4. Search Employee by Name")
        print("5. Update Employee Salary by Name")
        print("6. Exit")

    def start(self):
        while True:
            if not self.logged_in:
                self.login()
                if not self.logged_in:
                    continue

            self.show_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter employee's name: ")
                age = self.get_valid_age()
                salary = self.get_valid_salary()
                employee = Employee(name, age, salary)
                self.manager.add_employee(employee)

            elif choice == '2':
                self.manager.show_all_employees()

            elif choice == '3':
                min_age = int(input("Enter minimum age: "))
                max_age = int(input("Enter maximum age: "))
                self.manager.remove_employees_by_age_range(min_age, max_age)

            elif choice == '4':
                name = input("Enter employee's name to search: ")
                self.manager.search_employee_by_name(name)

            elif choice == '5':
                name = input("Enter employee's name to update salary: ")
                new_salary = float(input("Enter new salary: "))
                self.manager.update_salary_by_name(name, new_salary)

            elif choice == '6':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice, please try again.")

    def get_valid_age(self):
        while True:
            try:
                age = int(input("Enter employee's age: "))
                if age <= 0:
                    print("Age must be a positive number.")
                else:
                    return age
            except ValueError:
                print("Invalid input. Age must be a number.")

    def get_valid_salary(self):
        while True:
            try:
                salary = float(input("Enter employee's salary: "))
                if salary <= 0:
                    print("Salary must be a positive number.")
                else:
                    return salary
            except ValueError:
                print("Invalid input. Salary must be a number.")
