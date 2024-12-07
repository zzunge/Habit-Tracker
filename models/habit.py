import datetime

class Habit:
    def __init__(self, name, periodicity):
        self.name = name
        self.periodicity = periodicity  # "daily" or "weekly"
        self.creation_date = datetime.date.today()
        self.completion_history = []
        self.current_streak = 0

    def mark_complete(self):
        today = datetime.date.today()
        if today not in self.completion_history:
            self.completion_history.append(today)
            self.update_streak(today)

    def update_streak(self, date):
        if self.periodicity == "daily":
            expected_date = date - datetime.timedelta(days=1)
        elif self.periodicity == "weekly":
            expected_date = date - datetime.timedelta(weeks=1)

        if len(self.completion_history) > 1 and self.completion_history[-2] == expected_date:
            self.current_streak += 1
        else:
            self.current_streak = 1

    def is_broken(self):
        today = datetime.date.today()
        if not self.completion_history:
            return True
        last_completion = self.completion_history[-1]
        if self.periodicity == "daily":
            return (today - last_completion).days > 1
        elif self.periodicity == "weekly":
            return (today - last_completion).days > 7

    def to_dict(self):
        return {
            "name": self.name,
            "periodicity": self.periodicity,
            "creation_date": str(self.creation_date),
            "completion_history": [str(date) for date in self.completion_history],
            "current_streak": self.current_streak,
        }

    @staticmethod
    def from_dict(data):
        habit = Habit(data["name"], data["periodicity"])
        habit.creation_date = datetime.date.fromisoformat(data["creation_date"])
        habit.completion_history = [datetime.date.fromisoformat(d) for d in data["completion_history"]]
        habit.current_streak = data["current_streak"]
        return habit
