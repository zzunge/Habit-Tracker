import sys
import os

# Add the parent directory to the system path to allow imports from the models package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from models.habit import Habit

class TestHabit(unittest.TestCase):
    """
    Unit tests for the Habit class.
    """

    def test_habit_creation(self):
        """
        Test the initialization of a Habit object.

        Scenario:
        - Create a new Habit with the name "Exercise" and periodicity "daily".
        - Expected result: The habit name, periodicity, and current streak are set correctly.
        """
        # Create a habit instance
        habit = Habit("Exercise", "daily")

        # Assert that the attributes are initialized correctly
        self.assertEqual(habit.name, "Exercise")
        self.assertEqual(habit.periodicity, "daily")
        self.assertEqual(habit.current_streak, 0)

    def test_mark_complete(self):
        """
        Test the mark_complete method of the Habit class.

        Scenario:
        - Mark the habit as complete.
        - Expected result: The completion history contains one entry after marking complete.
        """
        # Create a habit instance
        habit = Habit("Exercise", "daily")

        # Mark the habit as complete
        habit.mark_complete()

        # Assert that the completion history contains one entry
        self.assertEqual(len(habit.completion_history), 1)

    def test_is_broken(self):
        """
        Test the is_broken method of the Habit class.

        Scenario:
        - Check if a habit with no completion history is considered broken.
        - Expected result: The habit is marked as broken (True).
        """
        # Create a habit instance
        habit = Habit("Exercise", "daily")

        # Assert that the habit is considered broken since it has no completions
        self.assertTrue(habit.is_broken())

if __name__ == "__main__":
    # Run the unit tests
    unittest.main()
