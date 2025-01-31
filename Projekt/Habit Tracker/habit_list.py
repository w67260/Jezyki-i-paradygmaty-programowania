from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QLabel
from database import load_habits

class HabitList(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lista nawyków")
        self.setGeometry(150, 150, 400, 400)

        layout = QVBoxLayout()

        self.habit_list = QListWidget()
        layout.addWidget(QLabel("Twoje nawyki:"))
        layout.addWidget(self.habit_list)

        self.setLayout(layout)
        self.load_habits()

    def load_habits(self):
        #Ładuje listę nawyków z CSV
        self.habit_list.clear()
        for habit in load_habits():
            progress_count = len(habit.progress)
            self.habit_list.addItem(f"{habit.name} - wykonano {progress_count} dni")
