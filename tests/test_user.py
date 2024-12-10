import sys
import os

# Add the parent directory to the system path to allow imports from the models package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from models.user import User
from models.habit import Habit
from tests.test_data_loader import load_test_data

class TestUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load test data and initialize a User object
        data = load_test_data()
        cls.user = User.from_dict(data)

    def test_add_habit(self):
        initial_count = len(self.user.habits)
        new_habit = Habit("New Habit", "daily")
        self.user.add_habit(new_habit)
        self.assertEqual(len(self.user.habits), initial_count + 1)

    def test_remove_habit(self):
        initial_count = len(self.user.habits)
        self.user.remove_habit("Exercise")
        self.assertEqual(len(self.user.habits), initial_count - 1)

if __name__ == "__main__":
    unittest.main()

