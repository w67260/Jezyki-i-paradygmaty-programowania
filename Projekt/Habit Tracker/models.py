class Habit:
    def __init__(self, id, name, description, frequency, created_at, progress):
        self.id = id
        self.name = name
        self.description = description
        self.frequency = frequency
        self.created_at = created_at
        self.progress = progress

    def mark_as_done(self, date):
        #Dodaje datę do listy wykonanych dni
        if date not in self.progress:
            self.progress.append(date)
