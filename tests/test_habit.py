import sys
import os

# Add the parent directory to the system path to allow imports from the models package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from models.habit import Habit
from tests.test_data_loader import load_test_data

class TestHabit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load test data
        data = load_test_data()
        cls.habit_data = data["habits"][0]  # Use the first habit for testing

    def test_habit_creation(self):
        habit = Habit.from_dict(self.habit_data)
        self.assertEqual(habit.name, "Exercise")
        self.assertEqual(habit.periodicity, "daily")

    def test_mark_complete(self):
        habit = Habit.from_dict(self.habit_data)
        habit.mark_complete()
        self.assertGreaterEqual(len(habit.completion_history), 1)

if __name__ == "__main__":
    unittest.main()

