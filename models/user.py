from models.habit import Habit

class User:
    def __init__(self, username):
        self.username = username
        self.habits = []

    def add_habit(self, habit):
        self.habits.append(habit)

    def remove_habit(self, habit_name):
        self.habits = [habit for habit in self.habits if habit.name != habit_name]

    def get_habit(self, habit_name):
        for habit in self.habits:
            if habit.name == habit_name:
                return habit
        return None

    def to_dict(self):
        return {
            "username": self.username,
            "habits": [habit.to_dict() for habit in self.habits],
        }

    @staticmethod
    def from_dict(data):
        user = User(data["username"])
        user.habits = [Habit.from_dict(h) for h in data["habits"]]
        return user
