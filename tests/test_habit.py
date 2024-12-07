import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from models.habit import Habit

class TestHabit(unittest.TestCase):
    def test_habit_creation(self):
        habit = Habit("Exercise", "daily")
        self.assertEqual(habit.name, "Exercise")
        self.assertEqual(habit.periodicity, "daily")
        self.assertEqual(habit.current_streak, 0)

    def test_mark_complete(self):
        habit = Habit("Exercise", "daily")
        habit.mark_complete()
        self.assertEqual(len(habit.completion_history), 1)

    def test_is_broken(self):
        habit = Habit("Exercise", "daily")
        self.assertTrue(habit.is_broken())  # Should be True since no completion yet

if __name__ == "__main__":
    unittest.main()
