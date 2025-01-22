import json

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

    def to_dict(self):
        return {"name": self.name, "age": self.age, "salary": self.salary}

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['age'], data['salary'])