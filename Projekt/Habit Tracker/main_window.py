from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QListWidget, QVBoxLayout, QWidget
from database import load_habits, add_habit, mark_habit_done
import sys
from datetime import datetime
from habit_form import HabitForm
from habit_list import HabitList

class HabitTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Habit Tracker")
        self.setGeometry(100, 100, 400, 500)

        self.habit_list = QListWidget()
        self.load_habits()

        self.add_button = QPushButton("Dodaj nawyk")
        self.add_button.clicked.connect(self.add_new_habit)

        self.mark_done_button = QPushButton("Oznacz jako wykonane")
        self.mark_done_button.clicked.connect(self.mark_habit_done)

        self.list_button = QPushButton("Pokaż nawyki")
        self.list_button.clicked.connect(self.show_habit_list)

        layout = QVBoxLayout()
        layout.addWidget(self.habit_list)
        layout.addWidget(self.add_button)
        layout.addWidget(self.mark_done_button)
        layout.addWidget(self.list_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def load_habits(self):
        #Ładuje nawyki do listy GUI
        self.habit_list.clear()
        for habit in load_habits():
            progress_days = len(habit.progress)
            self.habit_list.addItem(f"{habit.name} - wykonano {progress_days} dni")

    def add_new_habit(self):
        #Dodaje nowy nawyk
        add_habit("Nowy nawyk", "Opis", "daily")
        self.load_habits()

    def mark_habit_done(self):
        #Znacza wybrany nawyk jako wykonany
        selected_item = self.habit_list.currentRow()
        if selected_item >= 0:
            habits = load_habits()
            habit_id = habits[selected_item].id
            mark_habit_done(habit_id, datetime.today().strftime('%Y-%m-%d'))
            self.load_habits()

    def add_new_habit(self):
        #Otwiera formularz dodawania nawyku
        form = HabitForm(self)
        if form.exec():
            self.load_habits()

    def show_habit_list(self):
        #Otwiera okno listy nawyków
        self.list_window = HabitList()
        self.list_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HabitTracker()
    window.show()
    sys.exit(app.exec())
