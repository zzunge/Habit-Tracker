import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from models.user import User
from models.habit import Habit

class TestUser(unittest.TestCase):
    def test_add_habit(self):
        user = User("TestUser")
        habit = Habit("Exercise", "daily")
        user.add_habit(habit)
        self.assertEqual(len(user.habits), 1)

    def test_remove_habit(self):
        user = User("TestUser")
        habit = Habit("Exercise", "daily")
        user.add_habit(habit)
        user.remove_habit("Exercise")
        self.assertEqual(len(user.habits), 0)

if __name__ == "__main__":
    unittest.main()
