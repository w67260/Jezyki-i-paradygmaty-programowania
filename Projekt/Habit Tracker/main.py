import sys
import csv
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QListWidget, QVBoxLayout, QWidget, QLineEdit, QLabel, QMessageBox, QComboBox

CSV_FILE = "habits.csv"


class HabitTracker(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Habit Tracker")
        self.setGeometry(100, 100, 500, 500)

        #Główne okno
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        #Layout
        self.layout = QVBoxLayout()

        #Pole do wpisania nawyku
        self.habit_name_input = QLineEdit(self)
        self.habit_name_input.setPlaceholderText("Nazwa nawyku...")
        self.layout.addWidget(self.habit_name_input)

        #Pole do wpisania opisu
        self.habit_desc_input = QLineEdit(self)
        self.habit_desc_input.setPlaceholderText("Opis nawyku...")
        self.layout.addWidget(self.habit_desc_input)

        #Wybór częstotliwości
        self.frequency_dropdown = QComboBox(self)
        self.frequency_dropdown.addItems(["daily", "weekly", "monthly"])
        self.layout.addWidget(self.frequency_dropdown)

        #Przycisk dodawania nawyku
        self.add_button = QPushButton("Dodaj nawyk")
        self.add_button.clicked.connect(self.add_habit)
        self.layout.addWidget(self.add_button)

        #Lista nawyków
        self.habit_list = QListWidget(self)
        self.layout.addWidget(self.habit_list)

        #Przycisk usuwania wybranego nawyku
        self.delete_button = QPushButton("Usuń zaznaczony nawyk")
        self.delete_button.clicked.connect(self.delete_habit)
        self.layout.addWidget(self.delete_button)

        #Przycisk oznaczenia nawyku jako wykonany
        self.complete_button = QPushButton("Oznacz nawyk jako wykonany")
        self.complete_button.clicked.connect(self.mark_habit_completed)
        self.layout.addWidget(self.complete_button)

        self.central_widget.setLayout(self.layout)

        #Załaduj nawyki z pliku CSV
        self.load_habits()

    def add_habit(self):
        #Dodaje nowy nawyk do pliku CSV i odświeża listę
        name = self.habit_name_input.text().strip()
        description = self.habit_desc_input.text().strip()
        frequency = self.frequency_dropdown.currentText()
        created_at = datetime.today().strftime("%Y-%m-%d")
        progress = ""

        if name:
            habit_id = self.get_next_id()
            with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)
                writer.writerow([habit_id, name, description, frequency, created_at, progress])

            self.habit_name_input.clear()
            self.habit_desc_input.clear()
            self.load_habits()
        else:
            QMessageBox.warning(self, "Błąd", "Nazwa nawyku nie może być pusta!")

    def load_habits(self):
        #Wczytuje nawyki z pliku CSV i wyświetla je na liście
        self.habit_list.clear()

        try:
            with open(CSV_FILE, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file, quotechar='"', quoting=csv.QUOTE_MINIMAL)
                next(reader)
                for row in reader:
                    if row:
                        habit_id, name, description, frequency, created_at, progress = row
                        progress_display = progress if progress else "Brak postępu"
                        self.habit_list.addItem(f"{habit_id}. {name} - {frequency} (Postęp: {progress_display})")
        except FileNotFoundError:
            with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)
                writer.writerow(["id", "name", "description", "frequency", "created_at", "progress"])

    def delete_habit(self):
        #Usuwa zaznaczony nawyk z listy i z pliku CSV
        selected_item = self.habit_list.currentItem()

        if selected_item:
            habit_id = selected_item.text().split(".")[0]

            #Wczytaj wszystkie nawyki
            habits = []
            with open(CSV_FILE, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file, quotechar='"', quoting=csv.QUOTE_MINIMAL)
                habits = [row for row in reader if row and row[0] != habit_id]

            #Zapisz zmodyfikowaną listę
            with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)
                writer.writerows(habits)

            self.load_habits()
        else:
            QMessageBox.warning(self, "Błąd", "Nie wybrano żadnego nawyku!")

    def mark_habit_completed(self):
        #Oznacza wybrany nawyk jako wykonany, dodając datę do kolumny progress
        selected_item = self.habit_list.currentItem()

        if selected_item:
            habit_id = selected_item.text().split(".")[0]
            today = datetime.today().strftime("%Y-%m-%d")

            #Wczytaj nawyki i zaktualizuj postęp
            habits = []
            with open(CSV_FILE, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file, quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for row in reader:
                    if row and row[0] == habit_id:
                        row[-1] = f"{row[-1]};{today}" if row[-1] else today
                    habits.append(row)

            #Zapisz zmodyfikowaną listę
            with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)
                writer.writerows(habits)

            self.load_habits()
        else:
            QMessageBox.warning(self, "Błąd", "Nie wybrano żadnego nawyku!")

    def get_next_id(self):
        #Zwraca następne ID dla nowego nawyku
        try:
            with open(CSV_FILE, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file, quotechar='"', quoting=csv.QUOTE_MINIMAL)
                next(reader)
                ids = [int(row[0]) for row in reader if row]
                return max(ids) + 1 if ids else 1
        except FileNotFoundError:
            return 1


app = QApplication(sys.argv)
window = HabitTracker()
window.show()
sys.exit(app.exec())
