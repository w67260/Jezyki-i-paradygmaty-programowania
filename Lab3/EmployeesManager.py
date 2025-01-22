import json


class EmployeesManager:
    def __init__(self, filename='employees.json'):
        self.filename = filename
        self.employees = []
        self.load_employees()

    def add_employee(self, employee):
        if self.validate_employee(employee):
            self.employees.append(employee)
            self.save_employees()
        else:
            print("Invalid employee data. Could not add employee.")

    def show_all_employees(self):
        if not self.employees:
            print("No employees in the system.")
        else:
            for employee in self.employees:
                print(employee)

    def remove_employees_by_age_range(self, min_age, max_age):
        self.employees = [employee for employee in self.employees if not (min_age <= employee.age <= max_age)]
        self.save_employees()

    def search_employee_by_name(self, name):
        found = [employee for employee in self.employees if employee.name.lower() == name.lower()]
        if found:
            for employee in found:
                print(employee)
        else:
            print(f"No employee found with the name {name}.")

    def update_salary_by_name(self, name, new_salary):
        for employee in self.employees:
            if employee.name.lower() == name.lower():
                employee.salary = new_salary
                self.save_employees()
                print(f"Updated salary for {employee.name} to {new_salary}.")
                return
        print(f"No employee found with the name {name}.")

    def save_employees(self):
        with open(self.filename, 'w') as file:
            json.dump([employee.to_dict() for employee in self.employees], file, indent=4)

    def load_employees(self):
        try:
            with open(self.filename, 'r') as file:
                employees_data = json.load(file)
                self.employees = [Employee.from_dict(data) for data in employees_data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.employees = []

    def validate_employee(self, employee):
        if not isinstance(employee.age, int) or employee.age <= 0:
            print("Invalid age.")
            return False
        if not isinstance(employee.salary, (int, float)) or employee.salary <= 0:
            print("Invalid salary.")
            return False
        return True
