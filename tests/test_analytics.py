import sys
import os

# Add the parent directory to the system path to allow imports from the models package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from models.analytics import Analytics
from models.habit import Habit
from tests.test_data_loader import load_test_data

class TestAnalytics(unittest.TestCase):
    """
    Unit tests for the Analytics class.
    """
    @classmethod
    def setUpClass(cls):
        # Load test data from test_data.json
        data = load_test_data()
        cls.habits = [Habit.from_dict(habit) for habit in data["habits"]]

    def test_longest_streak(self):
        self.assertEqual(Analytics.longest_streak(self.habits), 5)

    def test_list_daily_habits(self):
        daily_habits = Analytics.list_daily_habits(self.habits)
        self.assertEqual(daily_habits, ["Exercise", "Meditate", "Drink Water"])
if __name__ == "__main__":
    # Run the unit tests
    unittest.main()
