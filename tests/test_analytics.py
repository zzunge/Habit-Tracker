import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from models.analytics import Analytics
from models.habit import Habit

class TestAnalytics(unittest.TestCase):
    def test_longest_streak(self):
        habits = [Habit("Exercise", "daily"), Habit("Read", "weekly")]
        habits[0].current_streak = 5
        habits[1].current_streak = 3
        self.assertEqual(Analytics.longest_streak(habits), 5)

    def test_list_daily_habits(self):
        habits = [Habit("Exercise", "daily"), Habit("Read", "weekly")]
        self.assertEqual(Analytics.list_daily_habits(habits), ["Exercise"])

if __name__ == "__main__":
    unittest.main()
