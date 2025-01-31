from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox
from database import add_habit

class HabitForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Dodaj nowy nawyk")
        self.setGeometry(150, 150, 300, 200)

        layout = QVBoxLayout()

        #Pole nazwy
        self.name_label = QLabel("Nazwa nawyku:")
        self.name_input = QLineEdit()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        #Pole opisu
        self.desc_label = QLabel("Opis:")
        self.desc_input = QLineEdit()
        layout.addWidget(self.desc_label)
        layout.addWidget(self.desc_input)

        #Częstotliwość
        self.freq_label = QLabel("Częstotliwość:")
        self.freq_input = QComboBox()
        self.freq_input.addItems(["Codziennie", "Co 2 dni", "Co tydzień"])
        layout.addWidget(self.freq_label)
        layout.addWidget(self.freq_input)

        #Przycisk dodawania
        self.add_button = QPushButton("Dodaj")
        self.add_button.clicked.connect(self.add_new_habit)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def add_new_habit(self):
        #Dodaje nowy nawyk i zamyka okno
        name = self.name_input.text()
        desc = self.desc_input.text()
        freq = self.freq_input.currentText().lower().replace(" ", "_")

        if name:
            add_habit(name, desc, freq)
            self.accept()
