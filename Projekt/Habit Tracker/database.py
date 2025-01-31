import csv
from models import Habit

CSV_FILE = "habits.csv"

def load_habits():
    #Wczytuje nawyki z pliku CSV i zwraca listę obiektów Habit
    habits = []
    try:
        with open(CSV_FILE, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                habit = Habit(
                    id=int(row["id"]),
                    name=row["name"],
                    description=row["description"],
                    frequency=row["frequency"],
                    created_at=row["created_at"],
                    progress=row["progress"].split(";") if row["progress"] else []
                )
                habits.append(habit)
    except FileNotFoundError:
        with open(CSV_FILE, "w", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["id", "name", "description", "frequency", "created_at", "progress"])
    return habits

def save_habits(habits):
    #Zapisuje listę nawyków do pliku CSV
    with open(CSV_FILE, "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["id", "name", "description", "frequency", "created_at", "progress"])
        for habit in habits:
            writer.writerow([habit.id, habit.name, habit.description, habit.frequency, habit.created_at, ";".join(habit.progress)])

def add_habit(name, description, frequency):
    #Dodaje nowy nawyk do pliku CSV
    habits = load_habits()
    new_id = max([h.id for h in habits], default=0) + 1
    new_habit = Habit(new_id, name, description, frequency, "2024-01-29", [])
    habits.append(new_habit)
    save_habits(habits)

def mark_habit_done(habit_id, date):
    #Oznacza nawyk jako wykonany w danym dniu
    habits = load_habits()
    for habit in habits:
        if habit.id == habit_id:
            habit.mark_as_done(date)
            break
    save_habits(habits)
